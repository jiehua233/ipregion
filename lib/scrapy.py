#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author   http://chenjiehua.me
# @date     2016-01
#

import sys
import time
import requests

from lib import ipip
from lib import utils

reload(sys)
sys.setdefaultencoding('utf8')


def parse_17monip():
    """ 从17monipdb.dat中获取ip数据段 """
    ipip.IP.load('./data/17monipdb.dat')
    max_comp_len = ipip.IP.offset - 1028
    ip0 = 0
    start, = ipip._unpack_V(ipip.IP.index[ip0*4:ip0*4 + 4])
    start = start * 8 + 1024
    s_int = 0
    with open('./data/monip.dat', 'wb') as f:
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
            f.write("%s\t%s\t%s\t%s\t%s\n" % (s_int, s, e_int, e, total))

            start += 8
            s_int = e_int + 1


def scrapy_tbip():
    with open('./data/tbip.dat', 'ab') as f:
        for line in xrange_monip():
            s = line.strip().split("\t")
            ip = {
                "si": s[0],
                "s": s[1],
                "ei": s[2],
                "e": s[3],
                "total": s[4],
            }
            ip.update(get_tbip_info(ip["s"]))
            info = '"%(si)s","%(ei)s","%(total)s","%(s)s","%(e)s","%(country)s\
","%(country_id)s","%(area)s","%(area_id)s","%(region)s","%(region_id)s","%(city)s\
","%(city_id)s","%(county)s","%(county_id)s","%(isp)s","%(isp_id)s"\n' % ip
            f.write(info)


def xrange_monip():
    with open('./data/monip.dat', 'rb') as f:
        for line in f:
            yield line.strip()


def get_tbip_info(ip):
    while True:
        url = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" % ip
        print 'get ip:', ip
        r = requests.get(url)
        try:
            result = r.json()
            if result['code'] == 0:
                return result['data']
            else:
                time.sleep(1)
        except:
            time.sleep(1)
