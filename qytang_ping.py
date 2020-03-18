#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import logging
import getpass
from kamene.all import *
from kamene.layers.inet import ICMP
from scapy.layers.inet import IP

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)

# 思路是copy上次learning的code


def qytang_ping(x):
    ping_pkt = IP(dst=x)/ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return True
    else:
        return False


if __name__ == '__main__':
    ip = getpass.getpass('Please input a IPv4 address:')
    # result = qytang_ping(ip)
    if qytang_ping(ip):
        print(ip, '通！')
    else:
        print(ip, '不通！')
