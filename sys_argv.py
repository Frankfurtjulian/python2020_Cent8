#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！


def sys_argv(a, b):
    print(int(a) + int(b))


if __name__ == '__main__':
    import sys
    print(sys.argv[0])
    sys_argv(sys.argv[1], sys.argv[2])
