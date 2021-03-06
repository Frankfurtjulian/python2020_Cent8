#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import logging
import getpass
from kamene.all import *
# from kamene.layers.inet import ICMP
# from scapy.layers.inet import IP

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)

# 思路是copy上次learning的code


def qytang_ping(x):
    ping_pkt = IP(dst=x)/ICMP()/(b'h'*100)  # 前两天发现ping不同外网，今天做类的时候才发现原来是ping包的size过小导致的
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return True
    else:
        return False


if __name__ == '__main__':
    # i = '192.168.213.128'
    i = getpass.getpass('Please input a IPv4 address:')
    # result = qytang_ping(ip)
    if qytang_ping(i):
        print(i, '通！')
    else:
        print(i, '不通！')


# import logging
# logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
# from scapy.all import *
#
#
# def qytang_ping(ip):
#     ping_pkt = IP(dst=ip) / ICMP()
#     ping_result = sr1(ping_pkt, timeout=2, verbose=False)
#     if ping_result:
#         return ip,1
#     else:
#         return ip,0
#
#
# if __name__ == '__main__':
#     result = qytang_ping('192.168.213.2')
#     if result[1]:
#         print(result[0], '通!')
#     else:
#         print(result[0], '不通!')