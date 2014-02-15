#!/usr/bin/env python
# -*- coding=UTF-8 -*-


import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

from generators.common import *


def weather_temp(soup):
    dic = {'TODAY': 0, 'TOMORROW': 1, 'AFTER': 2}
    t = repr(dic.get(findName(soup, 'TIME').text, 0))
    city = repr(findName(soup, 'CITY').text)
    dic2 = {'HIGH': 1, 'LOW': 0}
    key = repr(dic2.get(findName(soup, 'TYPE').text, 0))
    return 'weather.temperature(' + t + ', ' + \
            city + ')[' + key + ']'

def weather_describe(soup):
    dic = {'TODAY': 0, 'TOMORROW': 1, 'AFTER': 2}
    t = repr(dic.get(findName(soup, 'TIME').text, 0))
    city = repr(findName(soup, 'CITY').text)
    return 'weather.describe(' + t + ', ' + city + ')'

def weather_beijingaqi(soup):
    return funcToCode(soup, 'AQIquery')
