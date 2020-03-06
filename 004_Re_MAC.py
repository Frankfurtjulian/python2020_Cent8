#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import re

str1 = '166    54a2.74f7.0326       DYNAMIC     Gi1/0/11'
re_result1 = re.match(r'(\d+)\s+(\w{4}\.\w{4}\.\w{4})\s+(\w+)\s+(\S+\d)', str1).groups()


if __name__ == '__main__':
    print('-'*80)
    print('VLAN ID      :'  f'{re_result1[0]:<20}')
    print('MAC          :'  f'{re_result1[1]:<20}')
    print('TYPE         :'  f'{re_result1[2]:<20}')
    print('Interface    :'  f'{re_result1[3]:<20}')
