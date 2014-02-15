#!/usr/bin/env python
# -*- coding=UTF-8 -*-


import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

from upload_handler.generators.common import *
from upload_handler.generator import blockToCode, getUniqueVarName


def lists_create_empty(soup):
    return 'list()'

def lists_create_with(soup):
    num = int(soup.findChild('mutation')['count'])
    items = [valueToCode(soup, 'ADD' + str(x)) for x in xrange(num)]
    return '[' + ', '.join(items) + ']'

def lists_length(soup):
    return funcToCode(soup, 'len', 'VALUE')

def lists_isEmpty(soup):
    return lists_length(soup) + ' == 0'

def lists_getIndex(soup):
    return valueToCode(soup, 'VALUE') + '[' + \
            valueToCode(soup, 'AT') + ' - 1 ]'  # start from 1
