#-*- coding: utf-8 -*-

"""
requests.monkeys
~~~~~~~~~~~~~~~~

Urllib2 Monkey patches.

"""

import urllib.request, urllib.error, urllib.parse
import re

class Request(urllib.request.Request):
    """Hidden wrapper around the urllib2.Request object. Allows for manual
    setting of HTTP methods.
    """

    def __init__(self, url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None):
        urllib.request.Request.__init__(self, url, data, headers, origin_req_host, unverifiable)
        self.method = method

    def get_method(self):
        if self.method:
            return self.method

        return urllib.request.Request.get_method(self)


class HTTPRedirectHandler(urllib.request.HTTPRedirectHandler):
    """HTTP Redirect handler."""
    def _pass(self, req, fp, code, msg, headers):
        pass

    http_error_302 = _pass
    http_error_303 = _pass
    http_error_307 = _pass
    http_error_301 = _pass

