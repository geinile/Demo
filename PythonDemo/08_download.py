#使用urllib模块爬取简书首页图片

import os
from urllib import request
import re
import wget


def get_web(url, fname):
    #修改头部信息,因网站有防护被爬措施
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    r =request.Request(url, headers=headers)
    js_index = request.urlopen(r)

    with open(fname, 'wb') as fobj:
        while True:
            #防止文件太大,所有一次读取4k
            data = js_index.read(4096)
            if data:
                fobj.write(data)

def get_urls(fname, patt):
    #定义一个空列表,存匹配的字符
    patt_list = []
    #先编译要匹配的正则
    cpatt = re.compile(patt)

    with open(fname) as fobj:
        for line in fobj:
            #search匹配全部可以匹配的
            m = cpatt.search(line)
            if m:
                #使用group()方法输出匹配的信息,因search()匹配得到的是一个对象
                patt_list.append(m.group())

    return patt_list

if __name__ == '__main__':
    #将目录保存到dst模块,如果目录不存在就创建
    dst = '/tmp/jianshu'
    if not os.path.exists(dst):
        os.mkdir(dst)

    #通过urllib下载简述首页html文件
    get_web('https://jianshu.com/', '/tmp/js.html')

    #在网页中找到所有图片的地址
    patt = '//[\w/.-]+\.(png|jgp|jpeg|gif)'
    imgs_lists = get_urls('/tmp/js.html', patt)
    for img_url in imgs_lists:
        #匹配的url没有https:,使用字符串组合
        img_url = 'https:' + img_url
        wget.download(img_url, dst)




