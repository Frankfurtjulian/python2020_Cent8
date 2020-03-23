#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
from multiprocessing import Pool as ProcessPool
# from multiprocessing import freeze_support
import ipaddress
import pickle
from datetime import datetime
from Class_Ping import Qytping


def ping_scan(network):
    # 多进程
    pool = ProcessPool(processes=150)
    net = ipaddress.ip_network(network)

    result_obj_dict = {}

    for ip in net:
        # 获取返回的对象
        ping = Qytping(ip=str(ip))
        result_obj = pool.apply_async(ping.one())
        result_obj_dict[str(ip)] = result_obj

    pool.close()
    pool.join()

    print(result_obj_dict)

    active_ip = []

    for ip, obj in result_obj_dict.items():
        if obj.get()[1] == 1:
            active_ip.append(ip)

    print(active_ip)
    return active_ip


if __name__ == '__main__':
    now = datetime.now()
    ping_scan('192.168.213.0/24')
