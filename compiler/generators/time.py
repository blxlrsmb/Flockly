#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
# File: time.py
# Date: Sat Feb 15 20:24:01 2014 +0800
# Author: Yuxin Wu <ppwwyyxxc@gmail.com>

from datetime import datetime
from generators.common import valueToCode

def time_field(soup):
    field = findName(soup, 'FIELD').text
    if field not in ['year', 'month', 'day', 'hour', 'minute', 'second']:
        raise "Illegal Program!"
    dt = valueToCode(soup, 'DATETIME')
    return "({0}.{1})".format(dt, field)

def time_currentTime(soup):
    return 'currentTime()'

def time_lastTimeExecuted(soup):
    return 'lastTimeExecuted'

def time_totTimesExecuted(soup):
    return 'totTimesExecuted'

def time_time(soup):
    year = int(findName(soup, 'YEAR').text)
    month = int(findName(soup, 'MONTH').text)
    day = int(findName(soup, 'DAY').text)
    hour = int(findName(soup, 'HOUR').text)
    minute = int(findName(soup, 'MINUTE').text)
    return "datetime({0}, {1}, {2}, {3}, {4})".format(year, month, day, hour,
                                                     minute)
