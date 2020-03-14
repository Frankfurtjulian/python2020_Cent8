#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！

l1 = ['aaa', 111, (4, 5), 2.01]
l2 = ['bbb', 333, 111, 3.14, (4, 5)]

# 先从l1中一一取值并与l2对比，找出l1和l2共同的值，以及l1特有的
for x in l1:
    if x in l2:
        print(x, 'in l1 and l2')
    else:
        print(x, 'only in l1')
# 再从l2中一一取值，找出l2特有的
for y in l2:
    if y in l1:
        pass
    else:
        print(y, 'only in l2')

if __name__ == '__main__':
    pass
