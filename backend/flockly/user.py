#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# $File: user.py
# $Date: Fri Feb 14 21:45:46 2014 +0800
# $Author: Xiaoyu Liu <i[at]vuryleo[dot]com>

from mongoengine import *
import datetime
import time



class User(Document):
    userid = StringField(required=True, unique=True, primary_key=True)
    # name = StringField(required=True)
    access_token = StringField(required=True)
    access_token_expires = DateTimeField(default=datetime.datetime.now)
    def get_access_token():
        if time.time() < access_token_expires:
            return None
        else:
            return access_token

# vim: foldmethod=marker

