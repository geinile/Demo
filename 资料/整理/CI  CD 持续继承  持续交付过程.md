# CI / CD 持续继承 / 持续交付过程

- 使用技术：docker, gitlab

## 使用docker安装gitlab

- 安装gitlab至少需要4G内存

- 配置docker

  - 安装

    - 包由RHEL-extras提供
    - yum -y install docker
    - systemctl start / enable docker

  - 导入镜像

    - docker load < gitlab_zh.tar

  - 启动容器

    - 修改ssh服务端口为2022，因为需要使用ssh连接gitlab服务，且gitlab服务要使用443, 80端口

      - vim /etc/ssh/sshd_config
        - Port 2022		-> :wq
        - systemctl restart sshd

      ```shell
      docker run -d -h gitlab --name gitlab -p 443:443 -p 80:80 -p 22:22 --restart always -v /srv/gitlab/config:/etc/gitlab -v /srv/gitlab/logs:/var/log/gitlab -v /srv/gitlab/data:/var/opt/gitlab gitlab_zh:latest 
      #-d :在后台执行 -v ： 将文件映射到本机， - p 端口映射到本机
      #然后用docker ps 查看状态，当状态中显示healthy时，容器即可使用
      ```

  - 配置ssh免密上传代码

    - 生成ssh秘钥

      ```shell
      ssh-keygen -t rsa -C "wxiang_55@163.com" -b 4096
      ```
      
    - 设置 -> ssh秘钥 -> 将公钥拷贝到秘钥文本框即可
    
      ```shell
      cat /root/.ssh/id_rsa.pub
      ```
    
  - 上传代码
    
    ```shell
    #在gitlab上选择一个新仓库,且使用ssh连接
    echo "# - " README.md
    git init	#初始化
    git add README.md
    git commit -m "first commit"
    git remote add origin git@gitlab.com:devops/-.git
    git push -u origin master
    ```
    
    - 后续上传代码
    
      ```shell
      git add .
      git commit -m "add xxx"
      git push
      ```
    
  - 其他用户下载
    
    - 协议使用http
    - 第一次下载使用 git clone
    - 后续若有更新使用 git pull拉取即可
    
  - 若在使用git时不希望把某些文件、目录保存到版本库，可以在项目目录下创建.gitignore的文件，把需要忽略的文件写入即可
  
    ```shell
    *.doc
    *.docx
    ...
    ```
  
    

## 安装jenkins

1. jenkins它是当前最流行的一款持续集成(CI)工具

2. 自动化运维工具还有：ansible / docker / git / jenkins

3. jenkins是由Java编写，所以需要安装java-openjdk(1.5以上)

4. 装包起服务即可

   ```shell
   yum -y install jenkins
   systemctl start jenkins
   ss -neulp | grep :8080	#通过访问Jenkins的8080端口即可
   ```

5. 安装插件 -> 选择插件来安装 -> 无（因此时安装会连接外国资源，速度慢，后面改为国内）

6. 创建第一个用户管理员页面，点击使用admin

7. 进入后点击右上角configure修改密码

8. 在首页上点击manage jenkins -> manage plugins -> advanced -> update site中的url填写：https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/current/update-center.json -> submit

9. 点击Available选项卡，搜索找到[Localization: Chinese (Simplified)，该插件用于中文支持。

10. 点击Install without restart

11. 勾选Restart jenkins... ... 

12. 安装git parameter插件。用于访问git

## CI持续集成流程

1. 程序员编写代码，并推送到服务器

   - 在推送时，加标记

     ```shell
     ...
     git tag 1.0
     git push -u origin --tags 	#推送标记
     ```

     

2. Jenkins服务器下载代码

   ```shell
   新建项目 -> 构建一个自由风格的软件项目 
   1.General
   2.参数化构建过程	->	Name：webver	->	Parameter Type: Branch or Tag	->	Default Value: origin/master
   3.源码管理	->	Repository URL: http://192.168.1.89/devops/myweb.git	(此网站依据gitlab上填写)	->	Branches to build: $webver	->	Additional Behaviours: myweb-$webver
   4.构建	->	增加构建步骤	->	execute shell	->
   	#实现每个版本保存到不同的目录中
   	#且生成两个livever(当前版本）lastver(上一个版本）文件
   	dest=/var/www/html/deploy/packages	
   	cp -r myweb-$webver $dest   # 拷贝版本文件到web目录
   	cd $dest
   	rm -rf myweb-$webver/.git   # 删除版本库文件
   	tar czf myweb-$webver.tar.gz myweb-$webver  # 打包软件
   	rm -rf myweb-$webver   # 删除软件目录，因为只保留压缩包即可
   	md5sum myweb-$webver.tar.gz | awk '{print $1}' > myweb-$webver.tar.gz.md5  # 计算压缩包的md5值
   	cd ..
   	[ -f livever ] && cat livever > lastver  # 将livever内容写到lastver
   	echo $webver > livever   # 更新livever
   5.修改/var/www/html/deploy属主属组
   	chown -R jenkins.jenkins /var/www/html/devops/
   6.构建工程，测试
   ```

## CD持续交付过程

- 最好不把应用软件直接解压到目标，可以吧每个版本放到deploy目录下，网页主目录指向某一个版本的链接，想要发布哪个版本，只要把链接指向版本目录即可
- /var/www/download: 用于保存下载的软件包
- /var/www/deploy：用于保存livever版本文件和解压的软件包
- /var/www/html/nsd1902：指向某一版本目录的链接文件
- python脚本