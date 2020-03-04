#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import random


section1 = random.randint(1, 255)
section2 = random.randint(1, 255)
section3 = random.randint(1, 255)
section4 = random.randint(1, 255)

random_ip = str(section1) + '.' + str(section2) + '.' + str(section3) + '.' + str(section4)
# random_ip = section1 + '.' + section2 + '.' + section3 + '.' + section4


if __name__ == '__main__':
    print(random_ip)
