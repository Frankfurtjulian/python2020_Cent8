#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
from multiprocessing import Pool as ProcessPool
# from multiprocessing import freeze_support
import ipaddress
import pickle
from datetime import datetime
from scapy_ping_one_new import scapy_ping_one


def ping_scan(network):
    # 多进程
    pool = ProcessPool(processes=150)
    net = ipaddress.ip_network(network)

    result_obj_dict = {}

    for ip in net:
        # 获取返回的对象
        result_obj = pool.apply_async(scapy_ping_one, args=(str(ip),))
        result_obj_dict[str(ip)] = result_obj

    pool.close()
    pool.join()

    # print(result_obj_dict)

    active_ip = []

    for ip, obj in result_obj_dict.items():
        # print(obj.get())
        if obj.get()[1] == 1:
            active_ip.append(ip)

    # print(active_ip)
    return active_ip


if __name__ == '__main__':
    now = datetime.now()
    otherStyleTime = now.strftime("%Y-%m-%d_%H-%M-%S")
    scan_filename = 'sacn_save_pickle_' + otherStyleTime + '.pl'
    scan_file = open(scan_filename, 'wb')
    pickle.dump(ping_scan('192.168.213.0/26'), scan_file)
    scan_file.close()
    scan_file = open(scan_filename, 'rb')
    scan_result_list = pickle.load(scan_file)
    print(scan_result_list)
    # ping_scan('192.168.213.0/29')
