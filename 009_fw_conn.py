#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import re

fw_conn = 'TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO \n' \
          'TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO'

fw_conn_split = fw_conn.split('\n')
# fw_key = []
# fw_value = []
# fw_list = []
fw_dic = {}
for x in fw_conn_split:
    key1 = re.findall(r'\w+\s+\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)'
                      r'\s+\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)', x)
    value1 = re.findall(r'bytes\s+(\d+),\s+flags\s+(\w+)', x)
    # fw_dic = {key1[0]: value1[0]}
    fw_dic[key1[0]] = value1[0]

print(fw_dic)   # 打印字典

# 格式化打印
for k, v in fw_dic.items():
    print(f'{"src ":>10}:{k[0]:<20}|{"src_p ":>10}:{k[1]:<10}|{"dst ":>10}:{k[2]:<20}|{"dst_p ":>10}:{k[3]:<10}|\n'
          f'{"bytes ":>10}:{v[0]:<20}|{"flags ":>10}:{v[1]:<10}')
    print('='*110)

if __name__ == '__main__':
    pass
