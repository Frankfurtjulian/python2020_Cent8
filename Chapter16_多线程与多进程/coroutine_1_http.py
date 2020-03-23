#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import gevent
from gevent import monkey

monkey.patch_all()
import requests


def get_body(i):
    print("start", i)
    result = requests.get("http://www.qytang.com")
    print("end", i)
    return result


tasks = []

for i in range(3):
    tasks.append(gevent.spawn(get_body, i))
# tasks = [gevent.spawn(get_body, i) for i in range(3)]

all_result = gevent.joinall(tasks)
for x in all_result:
    print(x.get())
