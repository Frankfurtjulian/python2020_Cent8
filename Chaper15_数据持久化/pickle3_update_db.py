#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import pickle

dbfile = open('people-pickle.pl', 'rb')
db = pickle.load(dbfile)
dbfile.close()

print(db)

db['julian']['pay'] *= 1.6  # 提高工资

dbfile = open('people-pickle.pl', 'wb')
pickle.dump(db, dbfile)
dbfile.close()

if __name__ == '__main__':
    pass
