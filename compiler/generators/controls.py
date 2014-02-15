#!/usr/bin/env python
# -*- coding=UTF-8 -*-


import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

from upload_handler.generators.common import *
from upload_handler.generator import blockToCode, getUniqueVarName


def controls_if(soup):
    ret = ''
    _count = 0
    while True:
        if_value = findName(soup, 'IF' + str(_count))
        do_value = findName(soup, 'DO' + str(_count))
        if if_value is None:
            assert(_count > 0)  # at least one `if' statement
            break
        ret += ('if' if _count == 0 else 'elif')
        ret += ' (' + blockToCode(if_value.block) + '):\n'
        ret += indentCode(blockToCode(do_value.block))
        ret += '\n'
        _count += 1
    else_value = findName(soup, 'ELSE')
    if else_value:
        ret += 'else:\n'
        ret += indentCode(blockToCode(else_value.block))
    return ret


def controls_forEach(soup):
    return 'for ' + soup.findChild(attrs={'name': 'VAR'}).text + ' in ' + \
            valueToCode(soup, 'LIST') + ' :\n' + \
            indentCode(blockToCode(findName(soup, 'DO').block))


def controls_sleep(soup):
    return funcToCode(soup, 'time.sleep', ('SECS', int))


def controls_repeat(soup):
    times = findName(soup, 'TIMES').text
#use block's x position to name a temp var
    return 'for ' + getUniqueVarName() + ' in xrange(' + \
        times + '):\n' + \
        indentCode(blockToCode(findName(soup, 'DO').block))
