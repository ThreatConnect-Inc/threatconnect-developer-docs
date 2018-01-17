#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ipaddress


cidr_ranges = [{
    'input': 'abc:def:10::/48',
    'output': 'abc:def:10:0:0:0:0:0/48'
}, {
    'input': 'abc:0def:10::/48',
    'output': 'abc:def:10:0:0:0:0:0/48'
}, {
    'input': '0abc:def:10::/48',
    'output': 'abc:def:10:0:0:0:0:0/48'
}, {
    'input': 'abc:0def:10:000:00::/48',
    'output': 'abc:def:10:0:0:0:0:0/48'
}, {
    'input': 'abc:def:10:0000:0000:0000:0000:0000/48',
    'output': 'abc:def:10:0:0:0:0:0/48'
}, {
    'input': '2001:db8:1234::/48',
    'output': '2001:db8:1234:0:0:0:0:0/48'
}, {
    'input': '2001:db8:1234:0000:0000:0000:0000:0000/48',
    'output': '2001:db8:1234:0:0:0:0:0/48'
},]


def test_cidr_range_cleaner():
    for cidr in cidr_ranges:
        formatted_range = str()

        new_list =[section.replace("0000", "xxxx").lstrip("0") for section in ipaddress.IPv6Network(cidr['input']).exploded.split(":")]

        formatted_range = ":".join(new_list)
        formatted_range = formatted_range.replace("xxxx", "0")

        assert formatted_range == cidr['output']
