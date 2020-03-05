#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！

department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_Python = 1234.3456

line1 = 'Department1    ' + 'name:' + f'{department1:<15}' + 'Manager:' + f'{depart1_m:<15}' + 'COURSE FEES:' + \
        f'{COURSE_FEES_SEC:<15.2f}' + 'The End!'
line2 = 'Department2    ' + 'name:' + f'{department2:<15}' + 'Manager:' + f'{depart2_m:<15}' + 'COURSE FEES:' + \
        f'{COURSE_FEES_Python:<15.2f}' + 'The End!'


if __name__ == '__main__':
    length = len(line1)
    print('='*length)
    print(line1)
    print(line2)
    print('='*length)
