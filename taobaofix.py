#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
该脚本作用:
    合并相邻ip段,减少数据量
"""

import torndb
import utils

db = torndb.Connection('localhost', 'ip2loc', 'root', 'jiehua123')

def main():
    ips = db.query("SELECT * FROM `taobaoip`")
    pre = {}
    for ip in ips:
        print ip['id']

        if not pre:
            pre = ip
        elif dictequal(pre, ip):
            pre['total'] += ip['total']
        else:
            saved(pre)
            pre = ip


def dictequal(a, b):
    for key in ['country', 'country_id', 'area', 'area_id', 'region', 'region_id', 'city', 'city_id', 'county', 'county_id', 'isp', 'isp_id']:
        if a[key] != b[key]:
            return False
    return True


def saved(d):
    ei = d['start_int'] + d['total'] -1
    e = utils.int2ip(ei)
    save(d['start_int'], ei, d['total'], d['start'], e, d)


def save(si, ei, t, s, e, d):
    return db.execute("INSERT INTO `taobaoipfix`(`start_int`, `end_int`, `total`, `start`, `end`, `country`, `country_id`, `area`, `area_id`, `region`, `region_id`, `city`, `city_id`, `county`, `county_id`, `isp`, `isp_id`)"
                      "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", si, ei, t, s, e, d['country'], d['country_id'], d['area'], d['area_id'], d['region'], d['region_id'],
                      d['city'], d['city_id'], d['county'], d['county_id'], d['isp'], d['isp_id'])


if __name__ == "__main__":
    main()
