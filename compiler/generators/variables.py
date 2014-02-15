#!/usr/bin/env python
# -*- coding=UTF-8 -*-


import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

from generators.common import *

def variables_set(soup):
    ret = findName(soup, 'VAR').text + ' = '
    ret += valueToCode(soup, 'VALUE')
    return ret

def variables_get(soup):
    return findName(soup, 'VAR').text
