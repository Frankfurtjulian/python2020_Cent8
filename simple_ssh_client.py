#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
from qytang_ssh import qytang_ssh
from argparse import ArgumentParser

usage = "usage: python Simple_SSH_Client -i ipaddr -u username -p password -c command"

parser = ArgumentParser(usage=usage)

parser.add_argument("-i", "--ipaddr", dest="ip", help="SSH Server ipv4 Address", default='192.168.213.128', type=str)
parser.add_argument("-u", "--username", dest="username", help="SSH Username", default='root', type=str)
parser.add_argument("-p", "--password", dest="password", help="SSH Password", default='root', type=str)
parser.add_argument("-c", "--command", dest="cmd", help="SSH Command", default='ls', type=str)

args = parser.parse_args()

# output = qytang_ssh(args.ip, args.username, args.password, args.cmd)
# output = [args.ip, args.username, args.password, args.cmd]

if __name__ == '__main__':
    # print(output)
    print(qytang_ssh(ip=args.ip, username=args.username, password=args.password, cmd=args.cmd))
    # print(qytang_ssh(args.ip, args.username, args.password, args.cmd))  这个语句运行就有问题，貌似参数没有传过去......
