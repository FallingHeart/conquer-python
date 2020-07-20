# import collections
# collections太大了，我们引入其中的Counter就可以了
from collections import Counter
# Counter像Man一样是一个类，所以后面需要带括号来进行实例化
c = Counter()
# 现在c是一个Counter对象了
for i in 'programming':
    c[i] = c[i] + 1
    # 这里的i代表着遍历每个字符，当它是'p'的时候
    # c['p'] = c['p'] + 1
    # counter是dict的子类，其中所有的key:value初始值都为0
    # 即c['p'] = 0 + 1
    # 该语句将'p':0更新的值为'p':1
    # 如果接下去再遇到一个'p'那就会是c['p'] = 1 + 1
# 遍历完字符串查看结果
print(c)
# Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
# 调用Counter对象的update()方法，将对字符串'hello'的统计结果累计上去
c.update('hello')
# 查看更新后的结果
print(c)
# Counter({'r': 2, 'o': 2, 'g': 2, 'm': 2, 'l': 2, 'p': 1, 'a': 1, 'i': 1, 'n': 1, 'h': 1, 'e': 1})

import requests
# requests模块中有一个名为get的函数，其接收一个网址作为参数，返回一个response对象
r = requests.get(url='https://www.baidu.com/') # 百度首页
# 打印response对象的status_code,encoding属性
print(r.status_code,r.encoding)
# 200 ISO-8859-1
# 打印response对象的text,content属性
print(r.text)
print(r.content)
# '<!DOCTYPE html><!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8>...'
# b'<!DOCTYPE html>\r\n<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8>...'
# 对于诸如json之类特定类型的响应，可以通过执行response对象的json()方法直接获取
r = requests.get('https://market.douban.com/api/v2/cart/quantity')
json_content = r.json()
print(json_content)
# {'r': 1, 'error': '需要登录'}