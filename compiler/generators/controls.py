#!/usr/bin/env python
# -*- coding=UTF-8 -*-


import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

from generators.common import *


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

def controls_repeat_ext(soup):
    times = findName(soup, 'TIMES').text
#use block's x position to name a temp var
    return 'for ' + getUniqueVarName() + ' in xrange(' + \
        times + '):\n' + \
        indentCode(blockToCode(findName(soup, 'DO').block))

def controls_whileUntil(soup):
    mode = findName(soup, 'MODE').text  # 'WHILE', 'UNTIL'
    cond = valueToCode(soup, 'BOOL')
    do = blockToCode(findName(soup, 'DO').block)
    if mode == 'WHILE':
        return "while {0}:\n".format(cond) + \
                indentCode(do)
    elif mode == 'UNTIL':
        do += "\nif {0}:\n".format(cond) + indentCode('break')
        return "while True:\n" + \
                indentCode(do)
