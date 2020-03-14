#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import os
import re

# 执行并返回命令route -n的结果
route_n_result = os.popen('route -n').read()
# print(route_n_result)
# (参考了上次learning的方法！)用正则表达式找到目的网络为0.0.0.0，Genmask为0.0.0.0，且Flags为UG的那行，提取Gatway
gateway = re.findall(r'0\.0\.0\.0\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+0\.0\.0\.0\s+UG', route_n_result)[0]

# 拼接字符串并打印
print('网关为：', gateway, sep='')
# print('网关为：', f'{gateway:<20}', sep='')

if __name__ == '__main__':
    pass
