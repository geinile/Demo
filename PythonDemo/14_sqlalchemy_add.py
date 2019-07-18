#用于创建类的实例

# from 13_sqlalchemy import Departments, Employees, Salary, Session

############################################
# # 创建会话实例，用于连接数据库
# session = Session()
#
# # 创建部门实例
# hr = Departments(dep_id=1, dep_name='人事部')
# ops = Departments(dep_id=2, dep_name='运维部')
# dev = Departments(dep_id=3, dep_name='开发部')
# qa = Departments(dep_id=4, dep_name='测试部')
# finance = Departments(dep_id=5, dep_name='财务部')
# market = Departments(dep_id=6, dep_name='市场部')
# sales = Departments(dep_id=7, dep_name='销售部')
#
# # 在数据库中创建记录
# deps = [hr, ops, dev, qa, finance, market, sales]
# session.add_all(deps)
# session.commit()   # 确认至数据库
############################################




# # 创建员工实例
# mxz = Employees(
#     emp_id=1,
#     emp_name='张一',
#     birth_date='1994-05-28',
#     email='z1@163.com',
#     dep_id=2
# )
# wj = Employees(
#     emp_id=2,
#     emp_name='张二',
#     birth_date='1996-03-21',
#     email='z2@qq.com',
#     dep_id=2
# )
# xzc = Employees(
#     emp_id=3,
#     emp_name='张三',
#     birth_date='1995-08-09',
#     email='z3@qq.com',
#     dep_id=3
# )
# llc = Employees(
#     emp_id=4,
#     emp_name='张四',
#     birth_date='1995-12-20',
#     email='z4@tedu.cn',
#     dep_id=2
# )
# yty = Employees(
#     emp_id=5,
#     emp_name='张五',
#     birth_date='1992-01-15',
#     email='z5@163.com',
#     dep_id=3
# )
# wxm = Employees(
#     emp_id=6,
#     emp_name='张六',
#     birth_date='1995-02-18',
#     email='z6@qq.com',
#     dep_id=1
# )
# lt = Employees(
#     emp_id=7,
#     emp_name='张七',
#     birth_date='1997-08-19',
#     email='z7@tedu.cn',
#     dep_id=3
# )
# wy = Employees(
#     emp_id=8,
#     emp_name='张八',
#     birth_date='1996-11-08',
#     email='z8@163.com',
#     dep_id=2
# )
# mzy = Employees(
#     emp_id=9,
#     emp_name='张九',
#     birth_date='1994-06-10',
#     email='z9@qq.com',
#     dep_id=4
# )
#
#
# # 在数据库中创建记录
# emps = [mxz, wj, xzc, llc, yty, wxm, lt, wy, mzy]
# session.add_all(emps)
# session.commit()   # 确认至数据库



# # 关闭会话
# session.close()
############################################

