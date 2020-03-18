#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！


class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def getlastname(self):
        return self.name.split()[-1]

    def giveraise(self, percent):
        self.pay *= (1.0 + percent)

    def __str__(self):
        return '<%s => %s >' % (self.__class__.__name__, self.name)


if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software')
    julian = Person('Julian Huang', 44, 50000, 'network')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    print(bob.name, julian.pay)

    print(bob.getlastname(), julian.getlastname())
    julian.giveraise(0.1)
    print(julian.pay)
