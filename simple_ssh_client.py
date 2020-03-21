#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
from qytang_ssh import qytang_ssh
from arg_parse import ArgumentParser

usage = "usage: python Simple_SSH_Client -i ipaddr -u username -p password -c command"

parser = ArgumentParser(usage=usage)

parser.add_argument("-i", "--ipaddr", dest="ip", help="SSH Server ipv4 Address", default='192.168.213.128', type=str)
parser.add_argument("-u", "--username", dest="username", help="SSH Username", default='root', type=str)
parser.add_argument("-p", "--password", dest="password", help="SSH Password", default='root', type=str)
parser.add_argument("-c", "--command", dest="cmd", help="SSH Password", default='ls', type=str)

args = parser.parse_args()


if __name__ == '__main__':
    print(qytang_ssh(args.ip, args.username, args.password, args.cmd))
