#多进程,多线程的区别

#####################################
#子进程,多进程
#####################################
# import os
# print('starting...')
# os.fork()                 #生成子进程
# 后续代码在父子进程中都会执行,所有会输出两个hello world
# print('hello world!')

#输出:
#starting...
#hello world!
#hello world!
#####################################

#####################################
# import os
# print('starting...')
# retval = os.fork()
# if retval:              #父进程的返回值非0
#     print('in parent')
# else:
#     print('in children')
#####################################

#####################################
# import os
# print('starting...')
# for i in range(3):
#     retval = os.fork()
#     if not retval:      #子进程的返回值为0
#         print('hello world!')
#         exit()          #子进程遇到exit后,后续代码不再执行
# print('Done')
#若使用子进程一定要加exit,否则子进程会在产生子进程
#会输出三次hello world,且是并行同时执行的
#####################################

#####################################
#孤儿进程:在其父进程执行完成或被终止后仍继续运行的一类进程。
#这些孤儿进程将被init进程(进程号为1)所收养，并由init进程对它们完成状态收集工作
#僵尸进程:是当子进程比父进程先结束，而父进程又没有回收子进程，释放子进程占用的资源，此时子进程将成为一个僵尸进程。
#如果父进程先退出，子进程被init接管，子进程退出后init会回收其占用的相关资源
#解决僵尸进程方法:尝试杀死父进程
#####################################
# import os
# import time
# print('starting....')
# retval = os.fork()
# if retval:
#     print('父进程')
#     time.sleep(60)  #父进程睡60秒
# else:
#     print('子进程')
#     time.sleep(15)  #子进程睡15秒,此时子进程睡15秒之后,父进程还没有结束睡眠,此时子进程就成僵尸进程了
#     exit()
#
# print('Done')
#####################################
#父进程通过waitpid(m, n)函数检测子进程,n=0:挂起父进程,n=1:不挂起父进程, m=-1表示与wait()一样的功能
#waitpid()的返回值:如果子进程尚未结束则返回0,否则返回子进程的PID
# import os
# import time
# print('starting...')
# retval = os.fork()
# if retval:
#     print('父进程')
#     time.sleep(10)
#     print('go on')
#     print(os.waitpid(-1, 0))    #0:表示挂起父进程,直到子进程退出
#     print('go go go')
#     time.sleep(5)
# else:
#     print('子进程')
#     time.sleep(15)
#     exit()
#
# print('Done')

# starting...
# 父进程
# 子进程
# go on
# (0, 0)
# 子进程结束
# Done
# 当
#返回的最终结果是:父进程和子进程一起执行,10秒后父进程执行完成,然后挂起,5秒后,等子进程执行完成后
#父进程在睡5秒,程序执行完毕,
#####################################
# import os
# import time
#
# print('starting...')
# retval = os.fork()
# if retval:
#     print('父进程')
#     time.sleep(10)
#     print('go on')
#     print(os.waitpid(-1, 1))    #不挂起父进程
#     time.sleep(10)
# else:
#     print('子进程')
#     time.sleep(15)
#     print('子进程结束')
#     exit()
#
# print('Done')
# starting...
# 父进程
# 子进程
# go on
# (0, 0)
# 子进程结束
# Done
#####################################




#####################################
#单进程单线程的ping
# import subprocess
#
# def ping(host):
#     result = subprocess.run('ping -c2 %s &> /dev/null' % host, shell=True)
#     if result.returncode == 0:
#         print('%s:up' % host)
#     else:
#         print('%s:down' % host)
# if __name__ == '__main__':
#     #使用()生成一个生成器对象,节省空间
#     ips = ('176.215.111.%s' % i for i in range(1, 255))
#     for ip in ips:
#         ping(ip)
#####################################


#####################################
#多进程单线程的ping
# import subprocess
# import os
# def ping(host):
#     result = subprocess.run('ping -c2 %s &> /dev/null' % host, shell=True)
#     if result.returncode == 0:
#         print('%s:up' % host)
#     else:
#         print('%s:down' % host)
#
# if __name__ == '__main__':
#     ips = ('176.215.111.%s' % i for i in range(1, 255))
#     for ip in ips:
#         retval = os.fork()
#         if not retval:
#             ping(ip)
#             exit()
#####################################
#多线程ping
# import subprocess
# import threading
# def ping(host):
#     result = subprocess.run('ping -c2 %s &> /dev/null' % host, shell=True)
#     if result.returncode == 0:
#         print('%s:up' % host)
#     else:
#         print('%s:down' % host)
# if __name__ == '__main__':
#     ips = ('176.215.111.%s' % i for i in range(1, 255))
#     for ip in ips:
#         t = threading.Thread(target=ping, args=(ip,))
#         t.start()       #相当于执行target(*args),即把所有参数拆开执行
#####################################
#多线程ping,class表示
# import subprocess
# import threading
# class Ping:
#     def __init__(self, host):
#         self.host = host
#
#
#     #当调用类()时,会执行__call__方法
#     def __call__(self):
#         result = subprocess.run('ping -c2 %s &> /dev/null' % self.host, shell=True)
#         if result.returncode == 0:
#             print('%s:up' % self.host)
#         else:
#             print('%s:down' % self.host)
#
# if __name__ == '__main__':
#     ips = ('176.215.111.%s' % i for i in range(1, 255))
#     for ip in ips:
#
#         t = threading.Thread(target=Ping(ip))
#         t.start()   #相当于执行target(),因target是Ping的实例化对象,所以即执行Ping(ip)
#####################################




