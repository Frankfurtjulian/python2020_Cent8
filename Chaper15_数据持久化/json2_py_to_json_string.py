#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
# Python对象转换JSON字符串
import json
from source_db import qyt_teachers  # 导入字典
# from datetime import datetime
from pprint import pprint

print(qyt_teachers)  # 打印字典
pprint(qyt_teachers, indent=4)  # 打印格式看上去更加简单明了，易理解
print(type(qyt_teachers))

# qyt_teachers.update({'datetime': datetime.now()})  # Json不能有奇怪的对象，比如datetime对象就不行，转不了Json字符串
qyt_teachers.update({'bool': True})


json_string = json.dumps(qyt_teachers, ensure_ascii=False, indent=4)  # Json打印出来层次更好一点，打印出来更易理解
print(json_string)
print(type(json_string))

dict_recv = json.loads(json_string)
print(dict_recv)
print(type(dict_recv))

