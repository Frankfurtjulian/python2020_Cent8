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


# 方案二：修改为函数的更加通用的方案

#
# def find_same(list1, list2):
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 print(i, ' in list1 and list2')
#                 break
#         else:
#             print(i, ' only in list1')
#
#
# if __name__ == '__main__':
#     x = ['aaa', 111, (4, 5), 2.01]
#     y = ['bbb', 333, 111, 3.14, (4, 5)]
#     find_same(x, y)
