# import pymysql
#
# #####################################
# #1.建立到数据库的连接
#
# #数据库用户授权:
# #grant all on test.* to root@'%' identified by 'a'
# conn = pymysql.connect(
#     host='192.168.1.10',           #数据库ip
#     port=3306,                  #端口
#     user='root',                #授权用户名
#     passwd='a',           #密码
#     db='test',               #要连接的数据库
#     charset='utf8'              #字符集
# )
# #####################################
#
# #2.创建游标，用于将来执行SQL语句
# cursor = conn.cursor()
# #####################################
#
# #####################################
# #3.编写需要执行的SQL语句
# #根据1NF,每个表都要有主键
#
# create_dep = '''CREATE TABLE departments(
# dep_id INT,
# dep_name VARCHAR(20),
# PRIMARY KEY(dep_id)
# )'''
# create_emp = '''CREATE TABLE employees(
# emp_id INT,
# emp_name VARCHAR(20),
# birth_date DATE,
# phone VARCHAR(11),
# email VARCHAR(50),
# dep_id INT,
# PRIMARY KEY(emp_id),
# FOREIGN KEY(dep_id) REFERENCES departments(dep_id)      #外键
# )'''
# create_sal = '''CREATE TABLE salary(
# id INT,
# date DATE,
# emp_id INT,
# basic INT,
# awards INT,
# PRIMARY KEY(id),
# FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
# )'''
# #####################################
#
#
# #####################################
# #4.执行SQL语句
# cursor.execute(create_dep)
# cursor.execute(create_emp)
# cursor.execute(create_sal)
# #####################################
#
# #####################################
# #5.确认,增删改都需要确认
# conn.commit()
# #####################################
#
# #####################################
# #6.关闭游标和连接
# cursor.close()
# conn.close()
# #####################################