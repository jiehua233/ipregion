#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
该脚本作用:
    将17monip数据库中d4字段(主要为大学信息)更新到taobaoip数据库的county字段中
"""

import torndb

db = torndb.Connection('localhost', 'ip2loc', 'root', 'jiehua123')

def main():
    ips = db.query("SELECT * FROM `17monip` WHERE `d4` != ''")
    for ip in ips:
        print ip['id'], ip['d4']
        tbip = db.get("SELECT * FROM `taobaoip` WHERE `start_int` = %s", ip['start_int'])
        if tbip['county'] == '':
            db.execute("UPDATE `taobaoip` SET `county` = %s, `county_id` = -2 WHERE `id` = %s", ip['d4'], tbip['id'])
        else:
            print 'exit: ' + tbip['county']


if __name__ == "__main__":
    main()
