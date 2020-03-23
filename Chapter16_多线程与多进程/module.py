#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import os
import time
import threading


def qyt_multi(x, y, z):  # 打印进程和线程ID
    print('pid tid ==>', os.getpid(), threading.currentThread().ident)
    i = 1
    sum_x_y_z = 0
    while i < 10:
        sum_x_y_z = x * y * z
        x += 1
        y += 1
        z += 1
        i += 1
        time.sleep(1)
    # 返回计算结果，进程号，线程号
    return sum_x_y_z, os.getpid(), threading.currentThread().ident


if __name__ == '__main__':
    print(qyt_multi(1, 2, 3))
