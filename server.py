#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author   http://chenjiehua.me
# @date     2016-01
#

""" falcon server api """

import torndb
import falcon
import ujson as json
from wsgiref import simple_server

import config


def validate_phonenum(req, resp, resource, params):
    phonenum = params.get('phonenum')
    if not phonenum:
        raise falcon.HTTPBadRequest('Error', 'Phone Num is required.')
    if not phonenum.isdigit():
        raise falcon.HTTPBadRequest('Error', 'Phone Num should be digits.')
    if len(phonenum) < 7 or len(phonenum) > 11:
        raise falcon.HTTPBadRequest('Error', 'Phone Num length should be 7~11')

    params['phonenum'] = phonenum[:7]


class PhoneResource(object):

    def __init__(self, ib):
        self.ib = torndb.Connection(**ib)

    @falcon.before(validate_phonenum)
    def on_get(self, req, resp, phonenum):
        info = self.ib.get('SELECT * FROM phonenum WHERE phone = %s', phonenum)
        if info is None:
            raise falcon.HTTPNotFound()

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(info)


app = falcon.API()
phone = PhoneResource(config.INFOBRIGHT)
app.add_route('/{phonenum}', phone)


if __name__ == "__main__":
    host = config.SERVER['host']
    port = config.SERVER['port']
    httpd = simple_server.make_server(host, port, app)
    httpd.serve_forever()
