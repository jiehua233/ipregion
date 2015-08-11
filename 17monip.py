#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils
import ipip
import torndb

db = torndb.Connection('localhost', 'ip2loc', 'root', 'jiehua123')

def main():
    ipip.IP.load('17monipdb.dat')
    max_comp_len = ipip.IP.offset - 1028
    ip0 = 0
    start, = ipip._unpack_V(ipip.IP.index[ip0*4:ip0*4 + 4])
    start = start * 8 + 1024
    s_int = 0
    while start < max_comp_len:
        int_ip, = ipip._unpack_N(ipip.IP.index[start:start+4])
        index_offset, = ipip._unpack_V(ipip.IP.index[start + 4:start + 7] + chr(0).encode('utf-8'))
        index_length, = ipip._unpack_C(ipip.IP.index[start + 7])
        res_offset = ipip.IP.offset +index_offset - 1024
        info = ipip.IP.binary[res_offset:res_offset+index_length].decode('utf-8')
        ip = utils.int2ip(int_ip)
        print ip, info

        e_int = int_ip
        total = e_int - s_int + 1
        s = utils.int2ip(s_int)
        e = utils.int2ip(e_int)
        d = ['', '', '', '']
        info = info.strip().split('\t')
        c = 0
        for i in info:
            d[c] = i
            c += 1

        db.execute("INSERT INTO `17monip`(`start_int`, `start`, `end_int`, `end`, `total`, `d1`, `d2`, `d3`, `d4`)"
                   "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", s_int, s, e_int, e, total, d[0], d[1], d[2], d[3])

        start += 8
        s_int = e_int + 1


if __name__ == "__main__":
    main()
