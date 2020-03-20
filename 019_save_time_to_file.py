#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import datetime

now = datetime.datetime.now()
# print(now)
content = (now - datetime.timedelta(days=5)).strftime('%F %T.%f')
# print(type(content))

filename = 'save_fivedayago_time_' + now.strftime('%F_%H-%M-%S') + '.txt'
# print(filename)

create_file = open(filename, 'w')
create_file.write(content)
create_file.close()

if __name__ == '__main__':
    pass
