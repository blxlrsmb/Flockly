#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# $File: blockly.py
# $Date: Fri Feb 14 22:05:33 2014 +0800
# $Author: Xiaoyu Liu <i[at]vuryleo[dot]com>

from mongoengine import *

class Blockly(Document):
    userid = StringField(required=True)
    content = StringField(default="")
    name = StringField()
    lastexecution = IntField(default=0)
    timesexecuted = IntField(default=0)
    logs = ListField(default=[])

# vim: foldmethod=marker

