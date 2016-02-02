#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author   http://chenjiehua.me
# @date     2016-01
#

""" falcon server api """

import falcon
import ujson as json
from wsgiref import simple_server
from statsd import StatsClient

import config
from lib import torndb
from lib import utils

statsd = StatsClient(**config.STATSD)

def validate_ip(req, resp, resource, params):
    ip = params.get("ip")
    try:
        params["ip"] = utils.ip2int(ip)
    except:
        raise falcon.HTTPBadRequest('Error', 'Illegal ip address')

class IpResource(object):

    ip_list = []

    def __init__(self, ib):
        self.ib = torndb.Connection(**ib)
        ipdat = self.ib.query("SELECT `start_int` FROM `ipregion` ORDER BY `start_int`")
        for ip in ipdat:
            self.ip_list.append(ip["start_int"])

    @statsd.timer("request")
    @falcon.before(validate_ip)
    def on_get(self, req, resp, ip):
        statsd.incr("query")
        ip_start = self.get_start(ip)
        with statsd.timer("sql_query"):
            info = self.ib.get('SELECT * FROM `ipregion` WHERE `start_int` = %s', ip_start)
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(info)

    def get_start(self, ip):
        """ 二分查找 """
        i, j = 0, len(self.ip_list)-1
        while True:
            m = (i+j) / 2
            # got it
            if ip >= self.ip_list[m] and ip < self.ip_list[m+1]:
                break;

            if ip < self.ip_list[m]:
                # on the left side
                j = m
            else:
                # on the right side
                i = m

        return self.ip_list[m]


app = falcon.API()
ip = IpResource(config.INFOBRIGHT)
app.add_route('/{ip}', ip)


if __name__ == "__main__":
    host = config.SERVER['host']
    port = config.SERVER['port']
    httpd = simple_server.make_server(host, port, app)
    httpd.serve_forever()
