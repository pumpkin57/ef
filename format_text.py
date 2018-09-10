# -*- coding:utf-8 -*-
# @Date: 2018/9/6 18:09
# @Author: Cathy.cui
# @File: format_text.py

h = "{1} {0} {1}".format("hello","world")
print(h)
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

print("网络名：{name}, 网址 {url}".format(name = "菜鸟",url = "www.baidu.com"))

site = {"name": "菜鸟教程", "url": "www.runoob.com", "user": "xixi"}
print("网站名：{name}, 地址 {url}".format(**site))

my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(9)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的

print(list(range(5)))