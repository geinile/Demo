# NGINX

## web服务器对比

- Unix和Linux平台下
  - Apache， Nginx， Tengine， Lighttpd， Tomcat， IBM WebSphere， Jboss
- Windows平台下
  - 微软的IIS(INternet Information Server)

## Nginx简介

- 是俄罗斯人编写的十分轻量级的HTTP服务器
- 是一个高性能的HTTP和反向代理服务器，同时也是一个IMAP / POP3 / SMTP代理服务器
- 官网： http://nginx.org

Nginx安装

- 依赖包：gcc pcre-devel openssl-devel

  ```shell
  ./configure --prefix=/usr/local/nginx\	#指定安装路径，默认也是此路径
  	--user=nginx \
  	--group=nginx \
  	--with-http_ssl_module	#支持加密功能
  make && make install
  ```

- nginx配置文件及目录

  - /usr/local/nginx	#安装目录
  - conf/nginx.conf    #主配置文件
  - html                         #网页目录
  - logs                          #日志文件
  - sbin/nginx              #启动脚本

- 常用选项

  - -V：查看编译参数
  - -c：指定配置文件， 启动服务
  - -s : 启 停 重启服务

- 源码安装过程

  - ./configure 挑选功能，在src目录下有所有程序的功能，选择所需功能后 ./configure过程会挑选相应的软件包，生成objs目录，将挑选的源码放到objs/src/下
  - make: 将objs/src的源码编译成二进制文件，生成一个可执行文件

- Nginx平滑升级

  - 即将编译后的可执行文件覆盖原程序，源程序做备份
  - 覆盖后make upgrade 或killall nginx -> /usr/local/nginx/sbin/nginx、

- Nginx配置文件结构

  ```shell
  #全局选项
  user nginx;	#进程所有者
  worker_process	1;	#启动进程数量
  error_log	/var/log/nginx/error.log	#错误日志
  pid /var/run/nginx.pid	#pid文件
  events	{
  	worker_connections	1024;	#单个进程最多并发量
  }
  #配置容器
  http{
  ...
  server {
  	listen 80;
  	server_name localhost;
  	location / {
  	root html;
  	index index.html index.htm;
  	}
    }
  }
  ```

- 用户认证配置

  ```shell
  location /{
  	root html;
  	index index.html index.htm;
  	auth_basic "input password";	#提示语
  	auth_basic_user_file /usr/local/nginx/pass; #认证信息保存文件
  }
  yum -y install httpd-tools
  htpasswd -c /usr/local/nginx/pass	tom	#-c 表示创建，创建之后再用-c会把之前的覆盖
  #若增加用户，去掉-c，表示追加
  htpasswd /usr/local/nginx/pass jerry
  ```

- Nginx虚拟主机

  - 基于域名的虚拟主机

    ```shell
    server {
    	listen 80;
    	server_name www.a.com;
    	...
    }
    server {
    	listen 80;
    	server_name www.b.com;
    	...
    }
    ```

  - 基于端口的虚拟主机

    ```shell
    server{
    	listen 8080;
    	server_name www.a.com;
    	...
    }
    server{
    	listen 8000;
    	server_name www.a.com
    	...
    }
    ```

  - 基于IP的虚拟主机

    ```shell
    server{
    	listen 192.168.1.1:80;
    	server_name www.a.com;
    	...
    }
    server{
    	listen 192.168.1.2:80;
    	server_name www.a.com
    }
    ```

  - HTTPS加密网站

    - 编码，所有的编码都是基于ASCII编码实现的

      - ASCII 0~127， 美国用
      - GB2312：中国编码
      - big-8：台湾编码
      - Unicode：万国码，utf-8是Unicode的一种实现方式

    - 加密算法：分对称加密，非对称加密，信息摘要

      - 对称加密：AES， DES：主要用于单机
      - 非对称加密：RSA， DSA：主要用于网络数据加密
      - 信息摘要：MD5，sha256... :主要用于数据完整性校验
        - md5与时间，权限，文件名无关，只与文件内容有关

    - 生成秘钥

      - ssl加密网站的核心技术是非对称生成秘钥，包括公钥，私钥，证书

        ```shell
      cd /usr/local/nginx/conf
        openssl genrsa > cert.key 2048	#生成私钥
        openssl req -new -x509 -key cert.key > cert.pem	#生成证书（公钥）
        ```

    - 配置文件
    
      ```shell
      server {
      	listen 443;
      	server_name www.a.com;
      	ssl_certificate cert.pem;	#定义证书文件
      	ssl_certificate_key cert.key;	#定义私钥文件
      	...
      	
      }
      ```
    
      ​	
  
- 部署LNMP

  - L：Linux
  - N：Nginx
  - M：Mariadb：mariadb-server mariadb mariadb-devel
  - P：php php-fpm php-mysql

- Nginx + FasrCGI

  - 工作流程
    1. Web Server启动时载入FastCGI进程管理器
    2. FastCGI进程管理器初始化，启动多个解释器进程
    3. 当客户端请求到达Web Server时，FastCGI进程管理器选择并连接到一个解释器
    4. FastCGI子进程完成处理后返回结果，将标准输出和错误信息从同一连接返回Web Server
  - FastCGI目前支持语言有php c/c++ java perl python ruby等
  - FastCGI缺点
    - 内存消耗大
      - 因为是多进程，所以比CGI多线程消耗更多的服务器内存，php-cgi解释器每进程消耗7-15M内存，将这个数字乘以50或100就是很大的内存数
      - nginx+php（fastcgi）服务器在三万并发连接下开10个nginx进程消耗150M内存(10 * 15)，开64个php-cgi消耗1280M内存（20 * 64)

  - 配置fastcgi

    ```shell
    vim /etc/php-fpm.d/www.conf
    [www]
    listen 127.0.0.1:9000
    listen.allowed_clients = 127.0.0.1
    
    user = apache
    group=apache
    pm = dynamic
    pm.max_children = 50
    pm.start_servers = 5
    pm.min_spare_servers = 5
    pm.max_spare_servers = 35
    ```

    ```shell
    #nginx配置
    location / {
    	root html;
    	index index.php index.html index.htm
    }
    location ~\.php {
    	root html;
    	fastcgi_pass 127.0.0.1:9000;	#php-fpm的IP与端口
    	fastcgi_index index.php;
    	include fastcgi.conf;		#加载fast-cgi参数文件
    }
    ```

- 地址重写

  - 什么是地址重写
    - 获得一个来访的url请求，然后改写成服务器可以处理的另一个URL的过程
  - 地址重写的好处
    - 缩短URL，隐藏实际路径提高安全性
    - 易于用户记忆和键入
    - 易于被搜索引擎收录

