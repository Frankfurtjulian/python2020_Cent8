#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
from xml.etree.ElementTree import parse

tree = parse('xml1.xml')  # 打开分析的XML文件

root = tree.getroot()  # 找到根位置

QYT_Teachers = {}
for elem in tree.iter(tag='师资'):  # 找到师资标签（tag）
    Teachers_list = []
    for elem_in in elem.iter(tag='老师'):  # 找到师资标签（tag）下的老师标签
        Teachers_list.append(elem_in.attrib['name'])  # 找到每一个老师的名字，添加进入列表
    QYT_Teachers[elem.attrib['name'][:-2]] = Teachers_list  # 把XX团队的“团队”两字去掉
    # 把老师名字的列表，添加到以部门为键的字典中，作为部门这个键所映射的值！

print(QYT_Teachers)

# 课程与方向映射的字典
kecheng_dict = {'Security CCNP': '安全',
                'Wireless CCNP': '无线',
                'DataCenter CCNP': '数据中心',
                'RS CCNP': '路由交换'}
QYT_Courses = {}
for elem in tree.iter(tag='课程'):  # 找到课程标签（tag）
    Courses_list = []
    for elem_in in elem.iter(tag='课程名'):  # 找到课程标签（tag）下的课程名标签
        Courses_list.append(elem_in.attrib['name'])  # 找到每一个课程的名字，添加进入列表
    QYT_Courses[kecheng_dict[elem.attrib['name']]] = Courses_list
    # 把课程名字的列表，添加到以课程方向为键的字典中，作为课程方向这个键所映射的值！

print(QYT_Courses)

if __name__ == '__main__':
    pass
