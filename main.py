#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author   http://chenjiehua.me
# @date     2016-01
#

import argparse

import config
from lib import torndb
from lib import scrapy
from lib import ib

def main():
    args = parse_cmdline()
    ib.ib = torndb.Connection(**config.INFOBRIGHT)

    if args.initdb:
        ib.init_infobright()

    if args.parse17monip:
        scrapy.parse_17monip()

    if args.scrapytbip:
        scrapy.scrapy_tbip()


def parse_cmdline():
    parser = argparse.ArgumentParser()
    parser.add_argument('--initdb', default=0, const=1, type=int, choices=[0, 1], nargs='?')
    parser.add_argument('--parse17monip', default=0, const=1, type=int, choices=[0, 1], nargs='?')
    parser.add_argument('--scrapytbip', default=0, const=1, type=int, choices=[0, 1], nargs='?')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
