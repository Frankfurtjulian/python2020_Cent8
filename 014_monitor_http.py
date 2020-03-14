#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import os
import re
import time

# 提取netstat -tulnp命令结果，以\n为分隔进行行拆分，组成列表，从第三行开始取数据分析
while True:
    try:
        result = os.popen('netstat -tulnp').read().strip().split('\n')[2:]
        for line in result:
            if re.findall(r'tcp', line) and re.findall(r':80', line):
                print('HTTP (TCP/80)服务已经被打开！')
                break  # 跳出当前的for/else循环语句
        else:
            print('等待一秒重新开始监控！')
            time.sleep(1)
            continue  # 继续返回while循环
        break  # 跳出while循环
    except KeyboardInterrupt:  # 参照教主作业指导增加输入ctrl+c键盘中断时的抑制语句
        print('接收到管理员的ctrl+c!')
        print('退出程序')


if __name__ == '__main__':
    pass
