#!/usr/bin/env python
# -*- coding: utf-8 -*-

import torndb
import requests
import time
import utils

db = torndb.Connection('localhost', 'ip2loc', 'root', 'jiehua123')

def main():
    ips = db.query("SELECT * FROM `17monip_fix` WHERE `id` > 98")
    for ip in ips:
        ip_s = ip['start_int']
        ip_e = ip['end_int']
        checkipse(ip_s, ip_e)


def checkipse(ip_s, ip_e):
    print ip_s
    ip_s_d = getinfo(ip_s)
    if compipse(ip_s, ip_e):
        total = ip_e - ip_s + 1
        save(ip_s, total, ip_s_d)
        return

    print '---------cut------------'
    ptr = ip_s + 1
    while True:
        ptr_d = getinfo(ptr)
        if dictequal(ip_s_d, ptr_d):
            ptr += 1
        else:
            total = ptr - ip_s
            save(ip_s, total, ip_s_d)
            checkipse(ptr, ip_e)
            break


def getinfo(ip):
    ip = utils.int2ip(ip)
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


def compipse(ip_s, ip_e):
    ip_m = (ip_s + ip_e)/2
    ip_s_d = getinfo(ip_s)
    ip_e_d = getinfo(ip_e)
    ip_m_d = getinfo(ip_m)
    if dictequal(ip_s_d, ip_m_d) and dictequal(ip_e_d, ip_m_d):
        return True
    else:
        return False


def dictequal(a, b):
    for key in ['country', 'country_id', 'area', 'area_id', 'region', 'region_id', 'city', 'city_id', 'county', 'county_id', 'isp', 'isp_id']:
        if a[key] != b[key]:
            return False
    return True


def save(ip_s, total, d):
    return db.execute("INSERT INTO `taobaoip`(`ip`, `total`, `country`, `country_id`, `area`, `area_id`, `region`, `region_id`, `city`, `city_id`, `county`, `county_id`, `isp`, `isp_id`)"
                      "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", ip_s, total, d['country'], d['country_id'], d['area'], d['area_id'], d['region'], d['region_id'],
                      d['city'], d['city_id'], d['county'], d['county_id'], d['isp'], d['isp_id'])


if __name__ == "__main__":
    main()
