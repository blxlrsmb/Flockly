#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# $File: user.py
# $Date: Fri Feb 14 21:45:46 2014 +0800
# $Author: Xiaoyu Liu <i[at]vuryleo[dot]com>

from mongoengine import *
import time



class User(Document):
    userid = StringField(required=True, unique=True, primary_key=True)
    # name = StringField(required=True)
    access_token = StringField(required=True)
    access_token_expires = IntField()
    def get_access_token(self):
        if time.time() > self.access_token_expires:
            return None
        else:
            return self.access_token

# vim: foldmethod=marker

