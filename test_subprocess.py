#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚本由黄猛编写，用于Python学习！
import subprocess
import io


# 此函数可以判断命令是正确的命令输出还是错误的命令输出，现在教主推荐使用subprocess来执行命令！
def system_cmd(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
    proc.wait()
    stream_stdout = io.TextIOWrapper(proc.stdout)
    stream_stderr = io.TextIOWrapper(proc.stderr)

    str_stdout = str(stream_stdout.read())
    str_stderr = str(stream_stderr.read())

    return str_stdout, str_stderr


if __name__ == '__main__':
    exec_cmd = 'pwd'
    print(system_cmd(exec_cmd))
    exec_cmd = 'pwd1'
    print(system_cmd(exec_cmd))
# ('/root/python2020\n', '') 命令执行成功输出，0号位有输出，1号位无输出
# ('', '/bin/sh: pwd1: command not found\n') 命令执行失败输出，0号位无输出，1号位有输出
