#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import shelve
from datetime import timedelta

db = shelve.open('people-shelve')
julian = db['julian']  # 读取数据库键’julian‘中的字典
julian['pay'] *= 1.6  # 更新字典
db['julian'] = julian  # 把更新后的字典重新写回数据库键
db.close()

db = shelve.open('people-shelve')
datetime_now = db['datetime']  # 读取数据库键’datetime‘中的时间对象
datetime_now += timedelta(days=4)  # 在原来的时间基础上加4天
db['datetime'] = datetime_now  # 把更新后的字典重新写回数据库键
db.close()

db = shelve.open('people-shelve')
print(db['datetime'])
db.close()

if __name__ == '__main__':
    pass
