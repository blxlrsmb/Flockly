#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
# File: fb.py
# Date: Sat Feb 15 16:36:58 2014 +0800
# Author: Yuxin Wu <ppwwyyxxc@gmail.com>

def fb_getFriends(soup):
    return 'getMyFriends()'

def fb_updateStatus(soup):
    content = valueToCode(soup, 'TEXT')
    return 'updateStatus(str({0}))'.format(content)

def fb_userInfo(soup):
    field = findName(soup, 'FIELD').text
# TODO check safe fields
    user = valueToCode(soup, 'USER')
    return '({0}.{1})'.format(user, field)

def fb_commentStatus(soup):
    status = valueToCode(soup, 'STATUS')
    content = valueToCode(soup, 'TEXT')
    return 'commentStatus({0}, str({1}))'.format(status, content)

def fb_getAllStatus(soup):
    return 'getAllStatus()'

def fb_statusInfo(soup):
    field = findName(soup, 'FIELD').text
#TODO check safe fields
    status = valueToCode(soup, 'STATUS')
    return '({0}.{1})'.format(status, field)

def fb_myself(soup):
    return 'myself()'
