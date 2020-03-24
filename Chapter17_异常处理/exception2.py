#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！


def find_index(obj, index):
    print(obj[index])


if __name__ == '__main__':
    import re
    try:
        find_index('qytang', 5)
    # except:  # 它会捕获所有异常. Even system exitcalls and Ctrl-C key combinations，不推荐！Pycharm也会提示错误！
    #     pass
    except Exception as e:  # Exception除了系统退出事件类（SystemExit, KeyboardInterrupt, GeneratorExit）外的所有异常都会被它捕获。
        print(e)
    else:
        print('没有任何错误发生！！！')
    finally:
        print('这个总是要打印的！！！')
