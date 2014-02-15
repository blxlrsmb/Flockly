#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
# File: weather.py
# Author: Yuxin Wu <ppwwyyxxc@gmail.com>
import json
import requests

qqweather = "http://sou.qq.com/online/get_weather.php?city="


class Weather(object):
    _day = ["today", "tomorrow", "after"]

    def __init__(self):
        pass

    def gen_dict(self, t_day, w_day, t_night, w_night):
        ret = {'temp_high': int(t_day),
               'day': w_day,
               'temp_low': int(t_night),
               'night': w_night}
        return ret

    def parse_forecast(self, data):
        return self.gen_dict(data['TMAX'], data['BWEA'],
                             data['TMIN'], data['EWEA'])

    def query(self, city):
        """city is a string

            return type:
            dict[now / today / tomorrow / after]
        """
        r = requests.get(qqweather + city)
        dic = json.loads(r.text)
        ret = {}
        ret['now'] = int(dic['real']['temperature'])
        future = dic['future']['forecast']
        ret['today'] = self.parse_forecast(future[0])
        ret['tomorrow'] = self.parse_forecast(future[1])
        ret['after'] = self.parse_forecast(future[2])
        return ret

    def now_temperature(self, city):
        """return int"""
        return self.query(city)['now']

    def temperature(self, day, city):
        """day = 0: today;    1: tomorrow
           return a tuple
        """
        ret = self.query(city)[self._day[day]]
        return (ret['temp_low'], ret['temp_high'])

    def describe(self, day, city):
        """return a string  to describe weather of the day"""
        return self.query(city)[self._day[day]]['day']


def log(x):
    print repr(x).decode('unicode-escape')

if __name__ == "__main__":
    w = Weather()
    s = w.query("杭州")
    log(s)
    s = w.describe(0, "beijng")
    log(s)
