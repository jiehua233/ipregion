#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author   http://chenjiehua.me
# @date     2016-01
#

import gzip
import logging
import argparse
import torndb
from lib import scrapy
from etc import config


logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO)
db = torndb.Connection(**config.MYSQL)


def main():
    args = parse_cmdline()

    if args.parse17monip:
        scrapy.parse_17monip()

    if args.scrapytbip:
        scrapy.scrapy_tbip()

    if args.loaddb:
        load_database()


def parse_cmdline():
    parser = argparse.ArgumentParser()
    parser.add_argument('--loaddb', default=0, const=1, type=int, choices=[0, 1], nargs='?')
    parser.add_argument('--parse17monip', default=0, const=1, type=int, choices=[0, 1], nargs='?')
    parser.add_argument('--scrapytbip', default=0, const=1, type=int, choices=[0, 1], nargs='?')
    args = parser.parse_args()
    return args


def load_database():
    logging.info("Truncate table...")
    db.execute("TRUNCATE `ipregion`")
    logging.info("Load data into table...")
    for r in xrange_row():
        try:
            db.execute(
                "INSERT INTO `ipregion`(`start_int`, `end_int`, `total`, `start`, `end`, "
                "`country`, `country_id`, `area`, `area_id`, `region`, `region_id`, `city`, "
                "`city_id`, `county`, `county_id`, `isp`, `isp_id`)VALUES(%s, %s, %s, %s, %s, "
                "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", r['si'], r['ei'], r['t'],
                r['s'], r['e'], r['c'], r['ci'], r['a'], r['ai'], r['r'], r['ri'], r['ci'],
                r['cii'], r['co'], r['coi'], r['isp'], r['ispi'])
        except Exception as e:
            logging.error("line: %s, err: %s", r, e)


def xrange_row():
    key = ['si', 'ei', 't', 's', 'e', 'c', 'ci', 'a', 'ai', 'r', 'ri', 'ci', 'cii', 'co', 'coi', 'isp', 'ispi']
    with gzip.open("data/tbip.dat.gz") as f:
        for line in f:
            s = line.strip().split(",")
            row = {}
            for i, k in enumerate(key):
                row[k] = s[i].strip('"')

            yield row


if __name__ == "__main__":
    main()
