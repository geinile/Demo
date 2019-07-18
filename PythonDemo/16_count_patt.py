'用于统计一个文件中某些字段出现的次数'
#使用函数式编程实现
import re

def count_patt(fname, patt):
    patt_dict = {}  #空字典用于保存匹配到的结果
    cpatt = re.compile(patt)

    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)  #使用re先编译要匹配的字段,方便后面使用
            if m:  # 如果匹配不到返回None，表示False,匹配到了，是True
                key = m.group()   # 取出模式
                # 模式不在字典中，计数1，在字典中，加1
                patt_dict[key] = patt_dict.get(key, 0) + 1
                # if key not in patt_dict:
                #     patt_dict[key] = 1
                # else:
                #     patt_dict[key] += 1

    return patt_dict

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 可匹配192.168.1.10, 也可匹配1234.56789.10.123456
    br = 'Firefox|MSIE|Chrome'
    ip_count = count_patt(fname, ip)
    br_count = count_patt(fname, br)
    print(ip_count)
    print(br_count)
