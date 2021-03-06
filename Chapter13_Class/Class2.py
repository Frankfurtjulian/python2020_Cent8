#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
from Class1 import Person


class Manager(Person):
    """
    继承Person类,
    带有自定义加薪的Person
    继承了通用的lastname， str
    """

    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')
        # 为Manager类产生的实例自动产生Job为’Manager‘

    def giveraise(self, percent, bonus=0.1):
        Person.giveraise(self, percent + bonus)
        # self.pay *= (1.0 + percent + bonus)


if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    sue = Person(name='Sue Jones', age=45, pay=40000)
    bob = Person('Bob Smith', 42, 30000, 'software')
    print(tom.job)
    print(tom)
    print(bob)
    # print(tom.getlastname())
    # print(bob.getlastname())
    # tom.giveraise(0.1)
    # print(tom.pay)
    # bob.giveraise(0.1)
    # print(bob.pay)
    # db = [bob, sue, tom]
    # for obj in db:
    #     obj.giveraise(0.2)
    #     print(obj.getlastname(), '=>', obj.pay)
