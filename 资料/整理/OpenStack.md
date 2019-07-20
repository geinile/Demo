# OpenStack

- OpenStack是一个由NASA（美国国家航空航天局）和Rackspace合作研发并发起的项目
- OpenStack是一套IaaS解决方案
- OpenStack是一个开源的云计算管理平台
- 以Apache许可证为授权

## OpenStack主要组件

- Horizon
  - 用于管理OpenStack各种服务，基于web的管理接口，通过图形界面实现创建用户，管理网络，启动实例等操作
- Keystone
  - 为其他服务提供认证和授权的集中身份管理服务
  - 也提供了集中的目录服务
  - 支持多种身份认证模式，如密码认证，令牌认证，以及AWS（亚马逊web服务）登陆
  - 为用户和其他服务提供了sso认证服务
- Neutron
  - 一种软件定义网络服务
  - 用于创建网络，子网，路由器，管理浮动IP地址
  - 可以实现虚拟交换机，虚拟路由器
  - 可用于在项目中创建VPN
- cinder
  - 为虚拟机管理存储卷的服务
  - 为运行在Nova中的实例提供永久的块存储
  - 可以通过快照进行数据备份
  - 经常应用在实例存储环境中，如数据库文件
- Glance
  - 扮演虚拟机的镜像注册的角色
  - 允许用户为直接存储拷贝服务器镜像
  - 这些镜像可以用于新建虚拟机的模板
- Nova
  - 在节点上用于管理虚拟机的服务
  - Nova是一个分布式的服务，能够与keystone交互实现认证，与glance交互实现镜像管理
  - Nova被设计成标准硬件上能够进行水平扩展
  - 启动实例时，若有需要则下载镜像

## OpenStack配置实验

- 虚拟机配置
  - OpenStack管理主机
    - 2cpu, 6G以上内存，50G硬盘，IP：192.168.1.10
  - nova01, nova02计算节点配置
    - 2cpu，4.5G内存，100G硬盘， IP：192.168.1.11 12

1. 配置DNS，所有虚拟机指向真机，且NDS服务器不能与OpenStack安装在同一台主机

   1. openstack: nameserver 192.168.1.254
   2. nova01: nameserver 192.168.1.254
   3. nova02: nameserver 192.168.1.254

2. 配置/etc/hosts文件，所有虚拟机一样

   ```shell
   vim /etc/hosts
   192.168.1.10 openstack
   192.168.1.11 nova01
   192.168.1.12 nova02
   ```

3. 配置NTP时间同步，所有虚拟机一样

   ```shell
   vim /etc/chronyd.conf
   server 192.168.1.254 iburst	#iburst表示快速同步
   #启动服务
   systemctl restart chonryd
   #查看状态
   chronyc sources -v	#出现*号代表NTP时间可用
   ```

4. 配置yum仓库

   ```shell
   CentOS7-1804.iso	#系统软件
   RHEL7-extras.iso	#提供Python依赖软件包
   RHEL7OSP-10.iso		#此光盘拥有众多目录，每个目录都是一个软件包，只有两个
   	#openstack主要软件仓库
   		rhel-7-server-openstack-10-rpms
   	#packstack软件仓库
   		rhel-7-server-openstack-10-devtools-rpms
   #装完有10670个包
   ```

5. 安装额外软件包

   - qemu-kvm
   - libvirt-daemon
   - libvirt-daemon-driver-qemu
   - libvirt-client
   - python-setuptools

6. 检查基础环境

   1. 是否卸载firewalld和networkmanager
   2. 检查配置主机网络参数（静态IP）
   3. 主机名必须能够相互ping通
   4. 主机yum源（4个，10670）
   5. 依赖包是否安装
   6. NTP服务器是否可用
   7. /etc/resolv.conf不能有search开头的行
   8. grep vmx /proc/cpuinfo 查看是否支持vmx（虚拟化）
   9. grep ssse3 /proc/cpuinfo， 若无，则在真机/etc/modprode.d/kvm-nested.conf加options kvm-intel nested=1

7. 安装openstack-packstack, 生成应答文件

   1. yum -y install openstack-packstack
   2. packstack --gen-answer-file=answer.ini

8. 配置packstack

   1. 修改应答文件

      ```shell
      42: CONFIG_SWIFT_INSTALL=n				#没有ceph，使用本地磁盘，所有n
      45: CONFIG_CEILOMETER_INSTALL=n			#收费相关
      49: CONFIG_AODH_INSTALL=n				#收费相关
      53: CONFIG_GNOCCHI_INSTALL=n			#收费相关
      75: CONFIG_NTP_SERVERS=192.168.1.254	#NTP服务器
      98: CONFIG_COMPUTE_HOSTS=192.168.1.11	#装Nova，即装虚拟机的机器
      102: CONFIG_NETWORK_HOSTS=192.168.1.10,192.168.1.11	#支持vxlan的机器
      333: CONFIG_KEYSTONE_ADMIN_PW=a			#admin密码
      840: CONFIG_NEUTRON_ML2_TYPE_DRIVERS=flat,vxlan	#支持的网络协议
      910: CONFIG_NEUTRON_OVS_BRIDGE_MAPPINGS=physnet1:br-ex	#定义的三层虚拟交换机
      921: CONFIG_NEUTRON_OVS_BRIDGE_IFACES=br-ex:eth0	#绑定eth0，用于虚拟机上网，相当于wan口
      1179: CONFIG_PROVISION_DEMO=n			#是否需要一个例子做指引
      ```

9. 一键部署OpenStack

   1. 若前期准备无误，则耐心等待即可

      ```shell
      packstack --answer-file=answer.ini
      ```

10. 网络管理

    ```shell
    #查看外部OVS网桥
    cat /etc/sysconfig/network-scripts/ifcfg-br-ex
    #查看外部OVS网桥端口
    cat /etc/sysconfig/network-scripte/ifcfg-eth0
    #验证OVS配置
    ovs-vsctl show
    ```

11. Horizon配置

    1. horizon是一个用以管理，控制OpenStack服务的web控制面板，也称之为DashBoard仪表盘

    2. 可以管理实例，镜像，创建秘钥对，对实例添加卷，操作swift容器等，除此之外，用户还可以在控制面板中使用终端（console）或vnc直接访问实例

    3. 基于Python的Django web框架开发

    4. 功能与特点

       1. 实例管理：创建，终止实例，查看终端日志，vnc连接，添加卷等
       2. 访问与安全管理：创建安全群组，管理秘钥对，设置浮动IP等
       3. 偏好设定：对虚拟硬件模块进行不同偏好设定
       4. 镜像管理：编辑或删除镜像
       5. 用户管理：创建用户等
       6. 卷管理：创建卷和快照
       7. 对象存储管理：创建，删除容器和对象

    5. horizon bug处理

       1. 安装虽然没出错，但默认无法打开horizon，这是软件的配置bug，解决：

          ```shell
          vim /etc/httpd/conf.d/15-horizon_vhost.conf
          WSGIProcessGroup apache
          WSGIApplicationGroup %{GLOBAL}		#<-- 这里添加
          #重新载入配置文件即可
          apachectl graceful
          ```

    6. 访问openstack即可：http://192.168.1.10，用户名：admin  密码：a

    7. 初始化环境变量

       ```shell
       source ~/keystonerc_admin
       env | grep OS
       #使用帮助
       openstack help
       ```

12. OpenStack创建虚拟机等见：https://github.com/geinile/Demo/blob/master/资料/openstack.pdf

    



