# 模块用法

- **shutil模块**

  - 复制

    - copyfileobj的实现原理

      ```python
      def copyfileobj(fsrc, fdst, length = 16*1024)
      	while True:
              buf = fsrc.read(length)
              if not buf:
                  break
              fdst.write(buf)
      ```

    - shutil.copyfile        #只拷贝文件内容

      ​	shurile.copyfile('/bin/ls', '/tmp/list')

    - shutil.copy             #既拷贝文件内容，又拷贝权限

      ​	shutil.copy('/bin/ls', '/tmp/list')

    - shutil.copy2          #相当于 cp -p 

      ​	shutil.copy2('/bin/ls', '/tmp/list')

    - shutile.copytree  #相当于cp -r

      ​	shutile.copytree('/usr/local/nginx/', '/tmp/nginx')

  - 移动和删除

    - shutil.move            #移动

      ​	shutil.move('/tmp/list', '/var/tmp/list')

    - shutil.rmtree        #相当于rm -rf,但不可单独删文件

      ​	shutil.rmtree('/usr/local/nginx')

    - 删除单个文件见os模块

      

- **subprocess模块**：用于调用系统命令

  - subprocess.run(['ls', '/home'])

  - subprocess.run('ls /home', shell=True)

  - subprocesss的返回值

    ```python
    import subprocess
    rc = subprocess.run('ping -c2 192.168.1.254 &> /dev/nill', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    rc.returncode		#相当于echo $?
    rc.stdout.decode()	#subprocess的标准输出，但输出类型是二进制，所以使用decode()转成str类型
    rc.stderr.decode()	#subprocess的标准错误输出
    ```

- **time模块**

  - time.localtime()	#将一个时间戳转换为当期时区的struct_time

  - time.strftime()      #转成指定格式

    ```python
    time.strftime('%Y-%m-%d %H:%M:%S')		#转成年：月：日 时：分：秒
    ```

  - time.strptime()     #字符串转成九元组格式

    ```python
    time.strptime('2019-09-12 12:30:00', '%y-%m-%d %H:%M:%S')
    ```

    | 格式 | 含义                      | 格式 | 含义                              |
    | :--- | ------------------------- | ---- | --------------------------------- |
    | %a   | 本地简化星期名称          | %m   | 月份（01-12）                     |
    | %A   | 本地完整星期名称          | %M   | 分钟数（00-59）                   |
    | %b   | 本地简化月份名称          | %S   | 秒（01-61）                       |
    | %B   | 本地完整月份名称          | %U   | 一年中星期数（00-53）             |
    | %c   | 本地相应的日期和时间      | %w   | 一个星期中第几天（0-6， 0是周日） |
    | %d   | 一个月中第几天（01-31）   | %x   | 本地相应日期                      |
    | %H   | 一天中第几个小时（00-23） | %X   | 本地相应时间                      |
    | %l   | 一天中第几个小时（01-12） | %y   | 去掉世纪的年份（00-99）           |
    | %j   | 一年中第几天（001-366）   | %Y   | 完整的年份                        |
    | %Z   | 时区的名字                | %p   | 本地am或pm的相应符                |

- **datetime模块**

  - 获取当前时间

    ```python
    import datetime							#写法太长
    t1 = datetime.datetime.now()			#获取当前时间
    from datetime import datetime
    t1 = datetime.now()						#年月日时分秒毫秒
    	若调用：t1.year, t1.mouth, t1.day, t1.hour, t1.minute, t1.second, t1.microsecond
    ```

  - 将datetime对象转成时间字符串

    ```python
    from datetime import datetime
    t1 = datetime.now()
    datetime.strftime(t1, '%Y-%m-%d %H:%N:%S')
    ```

  - 将时间字符串转成datetime对象

    ```python
    datetime.strptime('2019-07-12 12:30:00', ''%Y-%m-%d %H:%N:%S'')
    ```

  - 创建指定时间的datetime对象

    ```python
    t = datetime(2019, 7, 8)
    ```

  - 计算时间差额，如100天零4小时之前，100天零4小时之后是什么时候,timedelta

    ```python
    from datetime import datetime, timedelta
    dt = timedelta(days=100, hours=4)
    t = datetime.now()
    t - dt		#100天之前
    t + dt 		#100天之后
    ```

    

- **os模块**

  ```python
  import os
  os.getcwd()										#pwd
  os.listdir()									#ls
  os.listdir('/tmp')								#ls /tmp
  os.makedirs('/tmp/mydemo/mydir')				#mkdir -p
  os.mkdir('/tmp/demo')							#mkdir
  os.chdir('/tmp/mydemo/mydir')					#cd /tmp/mydemo/mydir
  os.mknod('hello')								#touch hello
  os.symlink('/etc/hosts', 'zhuji')				#ln -s /etc/hosts zhuji
  os.chmod('hello', 0o644)						#chmod 644 hello ,权限为八进制
  os.rename('hello', 'welcome')					#mv hello welcome
  os.rmdir('/tmp/demo')							#rm -rf /tmp/demo， 只能删空目录
  os.unlink('zhuji')								#unlink zhuji， 删除软链接
  os.remove('welcome')							#rm -f welcome,删除文件
  ```

- **os.path子模块**

  ```python
  os.path.abspath('.')							#当前路径的绝对路径
  os.path.split('/tmp/demo/abc.txt')				#路径切割
  os.path.dirname('/tmp/demo/abc.txt')			#获取目录 -> /tmp/demo
  os.path.basename('/tmp/demo/abc.txt')			#获取文件名 -> abc.txt
  os.path.join('/tmp/demo', 'abc.txt')			#路径拼接
  os.path.isdir('/etc')							#/etc/是目录？
  os.path.isfile('/etc/hosts')					#存在并且是文件？
  os.path.islink('/etc/passwd')					#存在并且是链接吗
  os.path.ismount('/')							#存在并且是挂载点？
  os.path.exists('/abcd')							#存在吗？
  ```

- **pickle模块**

  - 当写入文件时，只能写入字符串，写入其他类型的数据，就会报错，使用pickle模块可以吧任意的数据类型写到文件中，还能无损地取出

  ```python
  #写入数据
  import pickle
  shopping_list = ['apple', 'banana', 'orange']
  with open('/tmp/shop.data', 'wb') as fobj:
      pickle.dump(shopping_list, fobj)			#写入数据
  #读取数据，还是列表的形式
  import pickle
  with open('/tmp/shop.data', 'rb') as fobj:
      mylist = pickle.load(fobj)
  type(mylist)
  ```

- **re模块：正则模块**

  ```python
  import re
  re.match('f..', 'seafood is food')		#从开头匹配，只匹配一个
  re.search('f..', 'seafood is food')		#在任意位置匹配，匹配多个
  re.finditer('f..', 'seafood is food')	#匹配到的对象放到生成器中
  #以上三种方法匹配到的结果可以用group()函数读取
  m = match('f..', 'seafood is food')
  m.group()
  re.findall('f..', 'seafood is food')	#匹配到全部对象，返回列表
  re.split(' |\.', 'hello greet welcome.ni.hao')		#以空格和.作为分隔符分割字符串
  re.sub('X', 'bob', 'Hi X, ni hao X')	#替换，把X替换成bob
  ```

  

- **tarfile模块**

  - 实现打包压缩和解压缩，同事支持gzip / bzip2 / xz 格式

    ```python
    import tarfile
    #压缩
    tar = tarfile.open('/tmp/mytest.tar.gz', 'w:gz')	#用gzip压缩
    tar.add('/etc/hosts')		#压缩文件
    tar.add('/etc/security')	#压缩目录
    tar.close()					#关闭
    #解压
    tar = tarfile.open('/tmp/mytest.tar.gz')	#自动识别压缩格式，以读方式打开
    tar.extractall(path='/var/tmp')				#指定解压目录，默认解压到当前目录
    tar.close
    ```

    

- **hashlib**

  - 用于计算文件的哈希值：md5/ sha/ sha256/ sha512

  ```python
  import hashlib
  m = hashlib.nd5(b'123456')	#计算数字的hash值
  	m.hexdigest()
  #计算文件的md5值
  with open('/etc/passwd', 'rb') as fobj:
      data = fobj.read()
     
  m = hashlib.md5(data)
  m.hexdigest()
  #多次更新，计算数据的md5值
  m = hashlib.md5()
  m.update(b'12')
  m.update(b'34')
  m.update(b'56')
  m.update(b'78')
  ```

- **pymsql模块应用**

  - 使用pymysql模块，链接数据库，执行CRUD操作

  - CRUD：Create、Retrieve、Update、Delete

    1. 创建数据库，授权用户

       ```shell
       create database nsd1902 default charset utf8;
       grant all on nsd1902.* to root@'%' identified by 'a';
       ```

    2. 创建到服务器的连接

    3. 创建游标，可以理解游标就是打开文件时返回的文件对象，通过游标可以执行sql语句，对数据库进行CRUD

    4. 编写sql语句

    5. 执行sql语句

    6. 确认

    7. 关闭游标和连接

# 字符串方法

- 去除字符串两端空白字符:strip()

  ```python
  ' \t hello world!\n'.strip()
  ```

- 去除字符串左端空白字符:lstrip()

  ```python
  ' \t hello world!\n'.lstrip()
  ```

- 去除字符串右端空白字符:rstrip()

  ```python
  ' \t hello world!\n'.rstrip()
  ```

- 小写转大写:upper()

  ```python
  hi = 'hello world'
  hi.upper
  ```

- 大写转小写:lower()

  ```python
  hi = 'HELLO WORLD'
  hi.lower()
  ```

- 居中：center()

  ```python
  hi = 'hello world'
  hi.center(30)
  hi.center(30, '*')		#居中，以*填充
  ```

- 居左，居右:ljust(), rjust()

  ```python
  hi = 'hello world'
  hi.ljust(30)
  hi.rjust(30, '$')		#以$填充
  ```

- 判断开头和结尾:startswith(), endswith()

  ```python
  hi = 'hello world'
  hi.startswith('h')		#以'h'开头？
  hi.endswith('o')		#以'o'结尾？
  ```

- 替换：replace()

  ```python
  hi = 'hello world'
  hi.replace('l', 'm')	#把所以'l'替换为'm'
  ```

- 切割和拼接:split(), join()

  ```python
  hi = 'hello world'
  hi.split()			#默认以空格切割
  hi.split('.')		#以 . 切割
  '.'join(str_list)	#以点为分隔符进行拼接
  ```

- 判断：is...()

  ```python
  hi = 'hello world'
  hi.islower()		#全是小写？
  hi.isupper()		#全是大写？
  hi.isdigit()		#全是数字？
  ```




## 函数

- **匿名函数**

  ```python
  def add(a, b)
  	return a + b
  #若用匿名函数，即去掉return即可
  myadd = lambda x, y: x + y
  ```

- **filter()函数**

  - 用于数据过滤，filter(func, sqp)，将seq中的每一项作为func函数的参数进行过滤，如果func返回值是True就留下，否则过滤掉

    ```python
    from random import randint
    nums = [randint(1, 100) for i in range(10)]
    def func(x):
    	return True if x % 2 == 0 else False
    list(filter(func, nums))		#将奇数过滤掉
    list(filter(lambda x: True if x % 2 == 0 else False, nums))	#调用匿名函数也可实现
    ```

- **map函数**

  用于数据加工，map(func, seq)，将seq中的每一项作为func的参数，func将数据加工处理后返回

  ```python
  from random import randint
  nums = [randint(1, 100) for i in range(10)]
  def func(x):
      return x * 2
  list(map(func, nums))		#所有数乘以2
  list(lambda x: x * 2, nums)	#调用匿名函数也可实现
  ```

  



























