###############################################
#钉钉聊天机器人
###############################################


import json
import requests
import sys
import getpass


###############################################     1.
#发送一个文件的消息

# def send_msg(url, reminders, msg):
#     #类型为Content-Type,charset必须为utf8
#     headers = {'Content-Type': 'application/json;charset=utf-8'}
#     data = {
#         "msgtype": "text",                  # 发送消息类型为文本
#         "at": {
#             "atMobiles": reminders,
#             "isAtAll": False,               #不@所有人
#         },
#         "text": {
#             "content": msg,                 #消息正文
#         }
#     }
#     #调用requests的post方法,传输数据给服务器
#     #data=json.dumps(data),将数据转换为json格式,json.loads(xxx)将json格式转化为普通格式
#     r = requests.post(url, data=json.dumps(data), headers=headers)
#     return r.json()                         #服务器的返回信息，用于调试
#
# if __name__ == '__main__':
#     msg = sys.argv[1]               #通过位置参数接收要传输的数据
#     reminders = ['15055667788']     #特殊提醒要查看的人,就是@某人一下
#     url = getpass.getpass()         #钉钉机器人的token码,授权码,在钉钉机器人设置找到
#     print(send_msg(url, reminders, msg))    #输出执行状态信息
###############################################     1.

###############################################     2.
#发送一个字典格式的消息
# url = getpass.getpass()
# headers = {'Content-Type': 'application/json;charset=utf-8'}
# data = {
#     "msgtype": "link",                          #消息类型为link
#     "link": {
#         "text": "这个即将发布的新版本，创始人陈航（花名“无招”）称它为“红树林”。"
#                 "而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是“红树林”？",
#         #消息标题
#         "title": "时代的火车向前开",
#         #图片地址
#         "picUrl": "https://upload.jianshu.io/collections/images/1647427/WechatIMG13.jpeg",
#         #点击之后跳转的界面
#         "messageUrl": "http://fanyi.sogou.com"
#     }
# }
#
# r = requests.post(url, data=json.dumps(data), headers=headers)
###############################################     2.



###############################################     3.
#发送一个markdown格式的
# url = getpass.getpass()
# headers = {'Content-Type': 'application/json;charset=utf-8'}
# data = {
#      "msgtype": "markdown",
#      "markdown": {
#          "title":"杭州天气",                    #文件标题
#          "text": "#### 杭州天气 @156xxxx8827\n" +
#                  "> 9度，西北风1级，空气良89，相对温度73%\n\n" +       # > 表示引用
#                  "> ![screenshot](https://gw.alipayobjects.com/zos/skylark-tools/public/files/84111bbeba74743d2771ed4f062d1f25.png)\n"  +
#                  "> ###### 10点20分发布 [天气](http://www.thinkpage.cn/) \n"
#      },
#     "at": {                     #要@谁
#         "atMobiles": [
#             # "156xxxx8827",
#             # "189xxxx8325"
#         ],
#         "isAtAll": False
#     }
# }
#
# r = requests.post(url, json.dumps(data), headers=headers)
###############################################     3.


###############################################     4.
#发送一个跳转的
# url = getpass.getpass()
# headers = {'Content-Type': 'application/json;charset=utf-8'}
# data = {
#     "actionCard": {
#         "title": "乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身",
#         "text": """![screenshot](https://upload.jianshu.io/collections/images/1647427/WechatIMG13.jpeg)
#  ### 乔布斯 20 年前想打造的苹果咖啡厅
#  Apple Store 的设计正从原来满满的科技感走向生活化，而其生活化的走向其实可以追溯到 20 年前苹果一个建立咖啡馆的计划""",
#         "hideAvatar": "0",
#         "btnOrientation": "0",
#         "singleTitle" : "阅读全文",
#         "singleURL" : "https://www.dingtalk.com/"
#     },
#     "msgtype": "actionCard"
# }
# r = requests.post(url, data=json.dumps(data), headers=headers)
###############################################     4.