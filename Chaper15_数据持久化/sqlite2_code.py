#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import sqlite3
import os

if os.path.exists('qytangcode.sqlite'):
    os.remove('qytangcode.sqlite')

# 创建Python字典对象，把对象写入SQLite数据库
teachers_dict = [{'姓名': '黄猛', '年龄': '44', '部门': '安全', '职位': '讲师'},
                 {'姓名': '马兰', '年龄': '18', '部门': '内务部', '职位': '大内总管'},
                 {'姓名': '黄子杰', '年龄': '10', '部门': '教育部', '职位': '部长'}]

# 连接SQLite数据库
conn = sqlite3.connect('qytangcode.sqlite')
cursor = conn.cursor()

# 执行创建表的任务
cursor.execute("create table qytang_teachers_info (姓名 varchar(40), 年龄 int, 部门 varchar(40), 职位 varchar(40) )")

# 读取Python字典数据，并逐条写入SQLite数据库
for teacher in teachers_dict:
    name = teacher['姓名']
    age = teacher['年龄']
    department = teacher['部门']
    job = teacher['职位']
    cursor.execute(f"insert into qytang_teachers_info values ('{name}', {age}, '{department}', '{job}')")

# 读取整个qytang_teachers_info表的信息，并且打印
cursor.execute("select * from qytang_teachers_info")
yourresults = cursor.fetchall()

for teacher in yourresults:
    print(teacher)

# 基于单一条件搜索数据库表
cursor.execute("select 年龄 from qytang_teachers_info where 姓名 = '黄猛'")
yourresults = cursor.fetchall()

for age in yourresults:
    print(age[0])

# 基于多重条件搜索数据库表
cursor.execute("select 姓名 from qytang_teachers_info where 年龄 > 40 and 职位 = '讲师'")
yourresults = cursor.fetchall()

for name in yourresults:
    print(name[0])

# 删除表
cursor.execute("drop table qytang_teachers_info")

# 严重注意一定要提交，否则数据不会实际写入数据库
conn.commit()
