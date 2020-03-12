#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import re

port_list = ['eth 1/101/1/42', 'eth 1/101/1/26', 'eth 1/101/1/23', 'eth 1/101/1/7', 'eth 1/101/2/46', 'eth 1/101/1/34',
             'eth 1/101/1/18', 'eth 1/101/1/13', 'eth 1/101/1/32', 'eth 1/101/1/25', 'eth 1/101/1/45', 'eth 1/101/2/8']

print(sorted(port_list, key=lambda x: (int(re.match(r'^eth (\d)/(\d\d\d)/(\d)/(\d+)', x).groups()[2]),
                                       int(re.match(r'^eth (\d)/(\d\d\d)/(\d)/(\d+)', x).groups()[3]))))
# 这个需要好好理解lambda这个函数，它把port_list这个列表中每个值拿出来作为x，然后用re.match匹配x的每个数，取2和3位做排序sorted.

if __name__ == '__main__':
    pass
