#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！


def qyt_argparse(host, filename, iface):
    print(host)
    print(filename)
    print(iface)


if __name__ == '__main__':
    from argparse import ArgumentParser  # 导入类

    usage = "usage: python arg_parse.py -t host -f filename -i interface"

    parser = ArgumentParser(usage=usage)  # 基于类创建实例

    # 通过类的add_option方法添加选项
    parser.add_argument("-f", "--file", dest="filename", help="Write content to FILE", default='1.txt', type=str)
    parser.add_argument("-i", "--interface", dest="iface", help="Specify an interface", default=1, type=int)
    parser.add_argument("-t", "--host", dest="host", help="Specify an host", default='10.1.1.1', type=str)
    # parser.add_argument(nargs="?", dest="host", help="Specify an host ipv4 address", default='10.1.1.1', type=str)
    # parser.add_argument(nargs="*", dest="hosts", help="Specify some hosts", default='10.1.1.1 10.1.1.2', type=str)
    args = parser.parse_args()  # 通过类的parse_args方法分析并返回选项

    qyt_argparse(args.host, args.filename, args.iface)
    # qyt_argparse(args.hosts, args.filename, args.iface)

