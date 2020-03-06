#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import re

str1 = 'Port-channel1.189   192.168.189.254 YES CONFIG  up'

re_result = re.match(r'([A-Za-z]\S+\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+YES\s+CONFIG\s+([a-z]+)', str1).groups()


if __name__ == '__main__':
    print(type(re_result))
    print('-'*80)
    # print(re_result)
    print('接口       ：'f'{re_result[0]:<15}')
    print('IP地址     ：'f'{re_result[1]:<15}')
    print('状态       ：'f'{re_result[2]:<15}')



