#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import pickle

dbfile = open('people-pickle.pl', 'rb')
db = pickle.load(dbfile)
for key in db:
    print(key, '=>', db[key])

if __name__ == '__main__':
    pass
