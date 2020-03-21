#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
from initdata import julian, manuel, emma
import shelve
from datetime import datetime

db = shelve.open('people-shelve')
db['julian'] = julian
db['manuel'] = manuel
db['emma'] = emma
db['datetime'] = datetime.now()
db.close()

if __name__ == '__main__':
    pass
