#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import time

while True:
    try:
        time.sleep(2)
        print('Ctrl + C to stop')
    except KeyboardInterrupt:
        print('Received ctrl+c from Admin!')
        print('Quit App!')
        break

if __name__ == '__main__':
    pass
