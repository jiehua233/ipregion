#!/usr/bin/env python
# -*- coding: utf-8 -*-

import struct
from ipip import IP



def main():
    IP.load('17monipdb.dat')
    print IP.offset
    print len(IP.index)


if __name__ == "__main__":
    str = struct.pack('>i', 20)
    print repr(str)
    print len(str)
    main()
