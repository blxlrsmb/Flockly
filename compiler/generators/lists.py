#!/usr/bin/env python
# -*- coding=UTF-8 -*-


import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

from generators.common import *


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
    at = soup.findChild('mutation')['at']
    list_str = valueToCode(soup, 'VALUE')
    if at == 'true':
        se = findName(soup, 'WHERE').text
        index = valueToCode(soup, 'AT')
        if se == 'FROM_END':
            index = '(-' + index + ')'
        else:
            index = '(' + index + '- 1)'
        return list_str + '[' + \
                index + ']'  # start from 1
    else:
        se = findName(soup, 'WHERE').text
        if se == 'FIRST':
            return list_str + '[0]'
        elif se == 'END':
            return list_str + '[-1]'
        elif se == 'RANDOM':
            return 'random.choice(list_str)'
        else:
            raise "Illegal Input!"


