#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import logging
# import getpass
from kamene.all import *

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)


class Qytping:  # 把ping模块改成类
    def __init__(self, ip):
        self.ip = ip
        self.srcip = None
        self.length = 100
        self.pkt = IP(dst=self.ip, src=self.srcip) / ICMP() / (b'h' * self.length)

    def src(self, srcip):
        self.srcip = srcip

    def size(self, length):
        self.length = length

    def one(self):
        self.pkt = IP(dst=self.ip, src=self.srcip) / ICMP() / (b'h' * self.length)
        ping_result = sr1(self.pkt, timeout=2, verbose=False)
        if ping_result:
            print(self.ip, "可达！！！")
        else:
            print(self.ip, "不可达！！！")

    def ping(self):
        self.pkt = IP(dst=self.ip, src=self.srcip) / ICMP() / (b'h' * self.length)
        for i in range(0, 5):
            ping_result = sr1(self.pkt, timeout=2, verbose=False)
            if ping_result:
                print('!', end='', flush=True)
            else:
                print('.', end='', flush=True)
        print()

    def __str__(self):
        if not self.scrip:
            return '<{0} = > dstip: {1}, size: {2}>'.format(self.__class__.__name__, self.ip, self.length)
        else:
            return '<{0} => srcip: {1}, dstip: {2}, size: {3}>'.format(self.__class__.__name__, self.srcip, self.ip,
                                                                       self.length)


if __name__ == '__main__':
    # ping = Qytping('192.168.213.2')
    ping = Qytping('8.8.8.8')
    ping.one()
    ping.ping()
    # ping.size(200)
    # ping.src('1.1.1.1')
    # ping.ping()
