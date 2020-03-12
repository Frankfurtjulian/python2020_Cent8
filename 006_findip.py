#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import os
import re


ifconfig_result = os.popen('ifconfig' + ' ens33').read()
# ifconfig_result = os.popen('ifconfig' + ' lo').read()
re_findall_result = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)
# print(type(re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.(\d{1,3})', re_findall_result[0])[0]))

for ip in re_findall_result:
    if re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.(\d{1,3})', ip)[0] == '0':
        mask = ip
        # print(mask)
    elif re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.(\d{1,3})', ip)[0] == '255':
        broadcast = ip
        # print(broadcast)
    else:
        ipv4_ip = ip
        # print(ipv4_ip)
netmask = 'Network Mask'
bro = 'Broadcast'
ipadd = 'IPv4 Addr'
print(f'{netmask:>15}' + ' : ' + f'{mask:>20}')
print(f'{bro:>15}' + ' : ' + f'{broadcast:>20}')
print(f'{ipadd:>15}' + ' : ' + f'{ipv4_ip:>20}')
# print(broadcast)
# print(ipv4_ip)


if __name__ == '__main__':
    pass

