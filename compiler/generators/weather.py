#!/usr/bin/env python
# -*- coding=UTF-8 -*-

from generators.common import *
from plugins.weather import Weather

def weather(soup):
    city = findName(soup, 'CITY').text
    w = Weather()
    result = w.query(city)['temp']
    return repr(result)

