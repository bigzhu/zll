#!/usr/bin/python
# encoding=utf-8
# file_name=ssh.py

import sys
import os


def readConf():
    '''
    读取置文件
    '''
    ssh_info = []
    f = open(sys.path[0] + '/ssh.ini', 'r')
    for i in f:
        ssh_one_info = i.split()
        if(len(ssh_one_info) != 0):
            ssh_info.append(tuple(i.split()))
    f.close()
    return sorted(ssh_info, key=lambda by: by[1])


def ssh(ssh_info):
    user = ssh_info[0]
    ip = ssh_info[1]
    port = 22
    if len(ssh_info) > 4:
        port = ssh_info[4]
    command = "export TERM=xterm;ssh -p %s %s@%s" % (port, user, ip)
    print 'ssh 登录中......'
    os.system(command)


def printInfo(ssh_info):
    for i in ssh_info:
        if len(i)>4:
            print str(ssh_info.index(i)).ljust(4), i[0].ljust(10), i[1].ljust(16), i[2].ljust(10), i[3].ljust(16), i[4]
        else:
            print str(ssh_info.index(i)).ljust(4), i[0].ljust(10), i[1].ljust(16), i[2].ljust(10), i[3]


def select(ssh_infos):
    input = raw_input('请输入序列号 or ip or hostname (q 退出):')
    if(input == 'q'):
        exit(0)
    try:
        input = int(input)
        if input <= len(ssh_infos) and input > 0:
            ssh(ssh_infos[input])
            return
        else:
            input = str(input)
    except ValueError as verr:
        pass
        #print verr

    selected_ssh_infos = []
    for i in ssh_infos:
        index = i[1].find(input)
        if(index != -1):
            selected_ssh_infos.append(i)
    if(len(selected_ssh_infos) == 0):
        print '没找到和这个ip有近似的'
        select(ssh_infos)
    elif(len(selected_ssh_infos) == 1):  # 找到一个，直接登录
        ssh(selected_ssh_infos[0])
        return
    else:
        return select(selected_ssh_infos)  # 找到一堆，再过滤


if __name__ == "__main__":
    ssh_info = readConf()
    printInfo(ssh_info)
    if ssh_info is not None:
        select(ssh_info)
