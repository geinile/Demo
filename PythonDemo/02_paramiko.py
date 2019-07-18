import paramiko
import sys
import getpass
import threading
import os

# def rcmd(host, user='root', passwd=None, port=22, command=None):
#     ssh = paramiko.SSHClient()              #实例化
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())       #相当于输入yes
#     ssh.connect(host, username=user, password=passwd, port=port)    #连接远程主机
#     stdin, stdout, stderr = ssh.exec_command(command)               #输出信息是由三部分组成,输入,输出,错误
#     out = stdout.read()                                             #读取
#     err = stderr.read()
#     if out:
#         print('[\033[34;1m%s\033[0m] \033[32;1mOUT\033[0m:\n%s' % (host, out.decode())) #由于读取到的是二进制文件,所以用decode()函数得到列表
#     if err:
#         print('[\033[34;1m%s\033[0m] \033[31;1mERROR\033[0m:\n%s' % (host, err.decode()))
#     ssh.close()                                                     #执行完需要操作的命令之后断开连接
#
# if __name__ == '__main__':
#     if len(sys.argv) != 3:                                          #没有三个值就报错
#         print('Usage: %s ipfile "command"' % sys.argv[0])
#         exit(1)
#
#     if not os.path.isfile(sys.argv[1]):                             #输入的文件不存在报错
#         print('No such file: %s' % sys.argv[1])
#         exit(2)
#
#     ipfile = sys.argv[1]                                            #ip列表文件等于第一个参数
#     command = sys.argv[2]                                           #要执行的命令在第二个参数
#     passwd = getpass.getpass()                                      #密文输入密码
#     with open(ipfile) as fobj:                                      #以一个对象形式打开ip列表文件
#         for line in fobj:                                           #便利文本文档用for循环
#             ip = line.strip()                                       #去除行尾的\n，得到IP地址
#             #接收字典参数用kwargs,单元素元祖用加,
#             t = threading.Thread(target=rcmd, args=(ip,), kwargs={'passwd': passwd, 'command': command})
#             t.start()  # rcmd(*args, **kwargs)                      #执行多线程
#             # rcmd(ip, passwd=passwd, command=command)