#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import pickle
from datetime import date
from initdata import db

dbfile = open('people-pickle.pl', 'wb')
pickle.dump(db, dbfile)
dbfile.close()

dbfile = open('people-pickle-datetime.pl', 'wb')
pickle.dump({'today': date.today()}, dbfile)
dbfile.close()


# if __name__ == '__main__':
#     dbfile = open('people-pickle.pl', 'rb')
#     db_read = pickle.load(dbfile)
#     for key in db_read:
#         print(key, '=>', db_read[key])
