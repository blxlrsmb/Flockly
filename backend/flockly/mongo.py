#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# $File: mongo.py
# $Date: Fri Feb 14 20:24:26 2014 +0800
# $Author: Xiaoyu Liu <i[at]vuryleo[dot]com>

"""database connections"""

from mongoengine import connect
import config

connect(config.DATABASE_NAME)

# vim: foldmethod=marker

