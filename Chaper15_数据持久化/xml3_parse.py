#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import xmltodict
from pprint import pprint
# import jason
from xml.dom import minidom
# 推荐使用这种方法

xml_file = open('xml1.xml', 'r').read()  # 打开待分析的XML文件

xmldict = xmltodict.parse(xml_file, encoding='utf-8')  # 读取xml并转换到OrderedDict字典【有序字典】,由于有中文因此用utf-8编码
pprint(xmldict)

# 提取部门
departments = xmldict['root']['公司']['部门']

for depart in departments:
    print(depart['@name'])

sec_teachers = xmldict['root']['公司']['部门'][1]['师资']['老师']  # 提取老师
for sec_teacher in sec_teachers:
    print(sec_teacher['@name'])

#
xmldict['root']['公司']['部门'][1]['@name'] = '乾颐堂安全'  # 修改内容

# 写回XML
XML_File = open('xml1_modified.xml', 'w', encoding='utf-8')
XML_File.write(minidom.parseString(xmltodict.unparse(xmldict)).toprettyxml(indent='    '))
XML_File.close()
