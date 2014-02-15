#!/usr/bin/env python
# -*- coding=UTF-8 -*-


import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

from generators.common import *


def logic_boolean(soup):
    return ('True' if findName(soup, 'BOOL').text == 'TRUE' else 'False')


def logic_compare(soup):
    ops = {
            'EQ': ' == ',
            'NEQ': ' != ',
            'LT': ' < ',
            'LTE': ' <= ',
            'GT': ' > ',
            'GTE': ' >= '
            }
    ret = valueToCode(soup, 'A')
    ret += ops[findName(soup, 'B')['label']]
    ret += valueToCode(soup, 'B')
    return ret

def logic_operation(soup):
    ops = {
            'AND': ' and ',
            'OR': ' or '
            }
    ret = valueToCode(soup, 'A')
    ret += ops[findName(soup, 'B')['label']]
    ret += valueToCode(soup, 'B')
    return ret

def logic_negate(soup):
    ret = 'not '
    ret += valueToCode(soup, 'BOOL')
    return ret
