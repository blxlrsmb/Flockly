#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
# File: w.py
# Date: Sun Feb 16 01:06:06 2014 +0800
# Author: Yuxin Wu <ppwwyyxxc@gmail.com>

import json
import requests

APIURL = "http://api.openweathermap.org/data/2.5/weather?q="

class Weather(object):
    def query(self, city):
        r = requests.get(APIURL + city)
        dic = json.loads(r.text)
        ret = {}
        ret['temp_min'] = float(dic['main']['temp_min']) - 273.15
        ret['temp_max'] = float(dic['main']['temp_max']) - 273.15
        ret['temp'] = float(dic['main']['temp']) - 273.15
        return ret

def log(x):
    print repr(x).decode('unicode-escape')

if __name__ == "__main__":
    w = Weather()
    s = w.query("Singapore")
    log(s)
