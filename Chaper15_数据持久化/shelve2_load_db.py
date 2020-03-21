#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import shelve

db = shelve.open('people-shelve')
for key in db:
    print(key, '=>\n', db[key])

db.close()

if __name__ == '__main__':
    pass
