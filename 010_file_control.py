#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import os
# 创建文件
os.mkdir('testdir')
os.chdir('testdir')
qytang1 = open('qytang1', 'w')
qytang1.write('test file\n')
qytang1.write('this is qytang\n')
qytang1.close()
qytang2 = open('qytang2', 'w')
qytang2.write('test file\n')
qytang2.write('qytang python\n')
qytang2.close()
qytang3 = open('qytang3', 'w')
qytang3.write('test file\n')
qytang3.write('this is python\n')
qytang3.close()
os.mkdir('qytang4')
os.chdir('qytang4')
qytang40 = open('qytang40', 'w')
qytang40.write('test file\n')
qytang40.write('this is qytang\n')
qytang40.close()
os.chdir('..')
os.mkdir('qytang5')
os.chdir('qytang5')
qytang50 = open('qytang50', 'w')
qytang50.write('test file\n')
qytang50.write('this is qytang\n')
qytang50.close()
os.chdir('..')
print(os.listdir(os.getcwd()))
# os.chdir('testdir')
# file_list = os.listdir(os.getcwd())
# print(file_list)
# l1 = []
# for file in file_list:
#     if os.path.isfile(file):
#         if 'qytang' in open(file).read():
#             l1.append(file)
#
#
# print('文件中包含“qytang”关键字的文件为：')
# for x in l1:
#     print('    ' + x)

# 上次learning的时候写的方法1
# for file_or_dir in os.listdir(os.getcwd()):
#     if os.path.isfile(file_or_dir):
#         for line in open(file_or_dir):
#             if 'qytang' in line:
#                 print(file_or_dir)
#                 break

# 上次learning的时候写的方法2，使用了遍历os.walk
for root, dirs, files in os.walk(os.getcwd(), topdown=True):
    for name in files:
        for line in open(os.path.join(root, name)):
            if 'qytang' in line:
                print(os.path.join(root, name))  # 打印完整路径+文件名
                break

# # 完成清理工作
os.chdir('..')
for root, dirs, files in os.walk('testdir', topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))
os.removedirs('testdir')

if __name__ == '__main__':
    pass
