import smtplib
from email.header import Header
from email.mime.text import MIMEText
import getpass

##############################################
#以本机作为服务器发邮件
##############################################

##############################################
#邮件正文(纯文本形式)
# msg = MIMEText('python email test', 'plain', 'utf8')
#plain:表示纯文本
#utf8:表示编码
##############################################

##############################################
#邮件头部信息:发件人(From),收件人(To),主题(Subject)
# msg['From'] = Header('root', 'utf8')
# msg['To'] = Header('bob', 'utf8')
# msg['Subject'] = Header('py test', 'utf8')
##############################################

##############################################
#发邮件:邮件服务器,发件人,收件人
#使用本机作为服务器
# smtp = smtplib.SMTP('localhost')
# sender = 'root'
# receviers = ['root', 'bob']
# smtp.sendmail('root', receviers, msg.as_bytes())
##############################################



##############################################
    #连接网易服务器发邮件
##############################################
def send_mail(host, password, sender, receviers, body, subject):
    #邮件头部信息:发件人,收件人,主题
    msg = MIMEText(body, 'plain', 'utf8')
    msg['From'] = Header(sender, 'utf8')
    msg['To'] = Header(receivers, 'utf8')
    msg['Subject'] = Header(subject)

    #发邮件:邮件服务器,发件人,收件人
    smtp = smtplib.SMTP()   #实例化
    smtp.connect(host)      #连接
    smtp.login(sender, password)    #登录
    smtp.sendmail(sender, receivers, msg.as_bytes())    #发邮件

if __name__ == '__main__':
    sender = 'wxiang_55@163.com'        #发件人
    receivers = 'wxiang_55@163'         #收件人,(网易邮箱暂时布支持发别人,原因还未找出)
    server = 'smtp.163.com'             #服务器
    password = getpass.getpass()        #密码
    body = 'hello from python'          #文件内容
    subject = 'python test email'       #主题
    send_mail(server, password, sender, receivers, body, subject)

