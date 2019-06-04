#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import check_token, _query_nodeping_api, config

API_URL = config.API_URL


def remove(token, checkid, customerid=None):
    """ Deletes a check with a give Check ID
    """

    check_token.is_valid(token)

    if customerid:
        url = "{0}checks/{1}?token={2}&customerid={3}".format(
            API_URL, checkid, token, customerid)
    else:
        url = "{0}checks/{1}?token={2}".format(API_URL, checkid, token)

    return _query_nodeping_api.delete(url)
