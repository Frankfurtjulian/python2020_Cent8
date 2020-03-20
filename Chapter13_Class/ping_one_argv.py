#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
from Class_Ping import Qytping


def ping_argv(ip):
    ping = Qytping(ip)
    ping.one()


if __name__ == '__main__':
    import sys
    ping_argv(sys.argv[1])
