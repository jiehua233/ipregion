#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ipip



def main():
    ipip.IP.load('17monipdb.dat')
    for i in range(256):
        o = i * 4
        start, = ipip._unpack_V(ipip.IP.index[o:o+4])
        print start

    print ipip.IP.offset
    print len(ipip.IP.index)


if __name__ == "__main__":
    main()
