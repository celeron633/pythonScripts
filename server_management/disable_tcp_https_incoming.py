#!/usr/bin/python3

import subprocess
import os
import sys

https_port_to_disable = [443, 1443, 2443, 3443, 4443, 5443, 6443, 7443, 8443, 9443, 10443]
ipt_template = 'iptables -t filter -A INPUT -p tcp --dport {} -j DROP'
ipt_disable_template = 'iptables -t filter -D INPUT -p tcp --dport {} -j DROP'

def enable():
    for port in https_port_to_disable:
        ipt_cmd = ipt_template.format(port)
        # print(ipt_cmd)
        
        cmd_list = []
        for item in ipt_cmd.split(' '):
            cmd_list.append(item)
        print(cmd_list)
        subprocess.run(cmd_list)

def disable():
    for port in https_port_to_disable:
        ipt_cmd = ipt_disable_template.format(port)
        # print(ipt_cmd)
        cmd_list = []
        for item in ipt_cmd.split(' '):
            cmd_list.append(item)
        print(cmd_list)
        subprocess.run(cmd_list)

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ['enable', 'disable']:
        print("usage: {} enable/disable".format(sys.argv[0]))
        exit(-1)

    if os.getuid() != 0:
        print('run as root!')
        exit(-1)

    if sys.argv[1] == 'enable':
        enable()
    elif sys.argv[1] == 'disable':
        disable()
