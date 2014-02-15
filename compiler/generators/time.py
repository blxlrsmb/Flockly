#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
# File: time.py
# Date: Sat Feb 15 16:53:32 2014 +0800
# Author: Yuxin Wu <ppwwyyxxc@gmail.com>

from datetime import datetime

def time_field(soup):
    field = findName(soup, 'FIELD').text
    if field not in ['year', 'month', 'day', 'hour', 'minute', 'second']:
        raise "Illegal Program!"
    print soup
    dt = valueToCode(soup, 'DATETIME')
    return "({0}.{1})".format(dt, field)

def time_currentTime(soup):
    return '(datetime.date(1, 1, 1))'

def time_lastTimeExecuted(soup):
    return '(datetime.date(1, 1, 1))'

def time_totTimesExecuted(soup):
    return '1'

