#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import os
import re

ifconfig_result = os.popen('ifconfig' + ' ens33').read()
mac = re.findall(r'ether\s+(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})', ifconfig_result)[0]
print(f'MAC地址为： {mac:<20}')

if __name__ == '__main__':
    pass
