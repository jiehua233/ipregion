#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ipip
import socket
import struct
import torndb

db = torndb.Connection('localhost', 'ip2loc', 'root', 'jiehua123')

def main():
    ipip.IP.load('17monipdb.dat')
    max_comp_len = ipip.IP.offset - 1028
    #start = 1024
    ip0 = 128
    start, = ipip._unpack_V(ipip.IP.index[ip0*4:ip0*4 + 4])
    start = start * 8 + 1024
    while start < max_comp_len:
        int_ip, = ipip._unpack_N(ipip.IP.index[start:start+4])
        index_offset, = ipip._unpack_V(ipip.IP.index[start + 4:start + 7] + chr(0).encode('utf-8'))
        index_length, = ipip._unpack_C(ipip.IP.index[start + 7])
        res_offset = ipip.IP.offset +index_offset - 1024
        info = ipip.IP.binary[res_offset:res_offset+index_length].decode('utf-8')
        ip = int2ip(int_ip)
        print ip, info
        db.execute("INSERT INTO `17monip`(`ip_end`, `ip_end_int`, `info`)"
                   "VALUES(%s, %s, %s)", ip, int_ip, info)
        start += 8

def ip2int(ip):
    return socket.ntohl(struct.unpack("I", socket.inet_aton(ip))[0])

def int2ip(int_ip):
    return socket.inet_ntoa(struct.pack("I", socket.htonl(int_ip)))


if __name__ == "__main__":
    main()
