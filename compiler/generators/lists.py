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

def lists_getIndex_new(soup):
    print soup
    mode = findName(soup, 'MODE').text
    at = soup.findChild('mutation')['at']
    list_str = valueToCode(soup, 'VALUE')
    if at == 'true':
        se = findName(soup, 'WHERE').text
        index = str(valueToCode(soup, 'AT'))
        if se == 'FROM_END':
            index = '(-' + index + ')'
        else:
            index = '(' + index + '- 1)'
    else:
        se = findName(soup, 'WHERE').text
        if se == 'FIRST':
            index = '0'
        elif se == 'END':
            index = '-1'
        else:
            raise "Illegal Input!"

    if mode == 'GET':
        return list_str + '[' + \
                index + ']'  # start from 1
    elif mode == 'REMOVE':
        return 'del ' + list_str + '[' + index + ']'
    elif mode == 'GET_REMOVE':
        return list_str + '.pop(' + index + ')'


