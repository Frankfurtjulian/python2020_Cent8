#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
from qytang_ping import qytang_ping
from qytang_ssh import qytang_ssh
import time
import getpass

ip = getpass.getpass("Input the Linux Server's IPv4 address:")
# print(qytang_ssh(ip, 'root', 'root', cmd='ls'))
# print(ip)
# result = qytang_ping(ip)
# print(result)
if qytang_ping(ip):
    # qytang_ssh(ip, 'root', 'root', 'ls')
    pass
else:
    qytang_ssh(ip, 'root', 'root', cmd='ls')
    # print(ip, '不可达！！！')


if __name__ == '__main__':
    pass
