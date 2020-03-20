#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import sys

system = sys.platform
if system == 'linux':
    print('This is linux!!!')
elif system == 'win32':
    print('This is windows!!!')
else:
    print('Other system!!')

if __name__ == '__main__':
    pass
