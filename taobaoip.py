#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
该脚本作用:
    根据17monip的ip段抓取淘宝数据,获取较为详细的ip数据
"""

import torndb
import requests
import time

db = torndb.Connection('localhost', 'ip2loc', 'root', 'jiehua123')

def main():
    ips = db.query("SELECT * FROM `17monip`")
    for ip in ips:
        print ip['id'], ip['start']
        ip_s_d = getinfo(ip['start'])
        save(ip['start_int'], ip['end_int'], ip['total'], ip['start'], ip['end'],ip_s_d)


def getinfo(ip):
    while True:
        url = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" % ip
        r = requests.get(url)
        try:
            result = r.json()
            if result['code'] == 0:
                return result['data']
            else:
                time.sleep(1)
        except:
            time.sleep(1)


def save(si, ei, t, s, e, d):
    return db.execute("INSERT INTO `taobaoip`(`start_int`, `end_int`, `total`, `start`, `end`, `country`, `country_id`, `area`, `area_id`, `region`, `region_id`, `city`, `city_id`, `county`, `county_id`, `isp`, `isp_id`)"
                      "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", si, ei, t, s, e, d['country'], d['country_id'], d['area'], d['area_id'], d['region'], d['region_id'],
                      d['city'], d['city_id'], d['county'], d['county_id'], d['isp'], d['isp_id'])


if __name__ == "__main__":
    main()
