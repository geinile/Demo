import pymysql

#通过pymysql模块连接数据库实现查询操作

##########################################
#1.建立到数据库的连接
# conn = pymysql.connect(
#     host='192.168.1.10',
#     port=3306,
#     user='root',
#     passwd='a',
#     db='test',
#     charset='utf8'
# )
##########################################


##########################################
#2.创建游标，用于将来执行SQL语句
# cursor = conn.cursor()

# 查询
# query_dep = 'SELECT * FROM departments'
# cursor.execute(query_dep)
# 取出数据
# result1 = cursor.fetchone()  # 取一行
# print(result1)
# print('*' * 40)
# result2 = cursor.fetchmany(2)  # 指定取出几行
# print(result2)
# print('*' * 40)
# result3 = cursor.fetchall()   # 取出全部
# print(result3)
##########################################


##########################################
#3.移动游标
# query_dep = 'SELECT * FROM departments'
# cursor.execute(query_dep)
# cursor.scroll(3, mode='absolute')   # 必须从开头算起，进行移动
# result = cursor.fetchone()
# print(result)
# print('*' * 40)
# cursor.scroll(1)   # 默认以相对当前位置移动
# result2 = cursor.fetchone()
# print(result2)
##########################################

##########################################
#4.关闭游标和连接
# cursor.close()
# conn.close()
