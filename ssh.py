#!/usr/bin/python
#encoding=utf-8
#file_name=ssh.py

import sys
import os


def init_ssh_info():
    ssh_info = []
    f = open(sys.path[0] + '/ssh.ini', 'r')
    for i in f:
        ssh_one_info = i.split()

        if(len(ssh_one_info) != 0):
            ssh_info.append(tuple(i.split()))
    f.close()
    return sorted(ssh_info, key=lambda by: by[1])


def ssh(user, ip, passwd):
    command = "export TERM=xterm;ssh %s@%s" % (user, ip)
    os.system(command)


def print_info(ssh_info):
    for i in ssh_info:
        print str(ssh_info.index(i)).ljust(4), i[0].ljust(10), i[1].ljust(16), i[2].ljust(10), i[3]


def select_nbr(ssh_info):
    print_info(ssh_info)
    nbr_input = raw_input('序号:')
    if(nbr_input == 'q'):
        exit(0)
    if(nbr_input == ''):
        if ssh_info is not None:
            select_ip(ssh_info)
    else:
        nbr = int(nbr_input)
        if(nbr > (len(ssh_info) - 1) or nbr < 0):
            print '序号的范围只是0到%s,请重新选择' % (len(ssh_info) - 1)
            select_nbr(ssh_info)
        ssh_info_one = ssh_info[nbr]

        user = ssh_info_one[0]
        ip = ssh_info_one[1]
        passwd = ssh_info_one[2]
        #ssh(ssh_info_one[0], ssh_info_one[1], ssh_info_one[2])
        return user, ip, passwd


def select_ip(ssh_info):
    ip_input = raw_input('ip(近似值):')
    if(ip_input == 'q'):
        exit(0)

    ssh_info_ip = []
    for i in ssh_info:
        index = i[1].find(ip_input)
        if(index != -1):
            ssh_info_ip.append(i)
    if(len(ssh_info_ip) == 0):
        print '没找到和这个ip有近似的'
        select_nbr(ssh_info)
    elif(len(ssh_info_ip) == 1):
        ssh_info_one = ssh_info_ip[0]
        user = ssh_info_one[0]
        ip = ssh_info_one[1]
        passwd = ssh_info_one[2]
        ssh(user, ip, passwd)
    else:
        return select_nbr(ssh_info_ip)


if __name__ == "__main__":
    ssh_info = init_ssh_info()
    print_info(ssh_info)
    if ssh_info is not None:
        user, ip, passwd = select_ip(ssh_info)
        ssh(user, ip, passwd)
