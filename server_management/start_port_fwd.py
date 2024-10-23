#!/usr/bin/python3

import subprocess
import os
import sys

fwd_map = {8080: {8081, 8082, 8083, 8084, 8085, 8086, 8087, 8088, 8089, 9090}, 443: {1443, 2443, 3443, 4443, 5443, 6443, 7443, 8443, 9443, 10443}}
ipt_template = 'iptables -t nat -A PREROUTING -p tcp --dport {} -j REDIRECT --to-port {}'
ipt_disable_template = 'iptables -t nat -D PREROUTING -p tcp --dport {} -j REDIRECT --to-port {}'

def enable():
    for dst_port in fwd_map:
        for src_port in fwd_map[dst_port]:
            ipt_cmd = ipt_template.format(src_port, dst_port)
            print(ipt_cmd)
            
            cmd_list = []
            for item in ipt_cmd.split(' '):
                cmd_list.append(item)
            print(cmd_list)
            subprocess.run(cmd_list)


def disable():
    for dst_port in fwd_map:
        for src_port in fwd_map[dst_port]:
            ipt_cmd = ipt_disable_template.format(src_port, dst_port)
            print(ipt_cmd)
            
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
