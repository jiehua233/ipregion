#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author   http://chenjiehua.me
# @date     2016-01
#

import os.path

ib = None

def init_infobright():
    drop_table('ipregion')
    create_table('ipregion')
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "tbip.dat")
    load_data_infile(file_path, 'ipregion')

def drop_table(table_name):
    ib.execute('DROP TABLE IF EXISTS `%s`' % table_name)

def create_table(table_name):
    ib.execute('''
CREATE TABLE IF NOT EXISTS `%s` (
`start_int` bigint(20) NOT NULL,
`end_int` bigint(20) NOT NULL,
`total` int(11) NOT NULL,
`start` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
`end` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
`country` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
`country_id` varchar(16) COLLATE utf8_unicode_ci DEFAULT NULL,
`area` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
`area_id` varchar(16) COLLATE utf8_unicode_ci DEFAULT NULL,
`region` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
`region_id` varchar(16) COLLATE utf8_unicode_ci DEFAULT NULL,
`city` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
`city_id` varchar(16) COLLATE utf8_unicode_ci DEFAULT NULL,
`county` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
`county_id` varchar(16) COLLATE utf8_unicode_ci DEFAULT NULL,
`isp` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
`isp_id` varchar(16) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=brighthouse DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
               ''' % table_name)

def load_data_infile(file_path, table_name):
    ib.execute(
        '''LOAD DATA LOCAL INFILE '%s' INTO TABLE %s FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\\n'
        ''' % (file_path, table_name))
