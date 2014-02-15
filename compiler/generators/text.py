#!/usr/bin/env python
# -*- coding=UTF-8 -*-


import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

from generators.common import *

def text(soup):
    return repr(findName(soup, 'TEXT').text)

def text_print(soup):
    to_print = valueToCode(soup, 'TEXT')
    return 'print {0}'.format(to_print)

def text_join(soup):
    num = int(soup.findChild('mutation')['item'])
    texts = [valueToCode(soup, 'ADD' + str(x)) for x in xrange(num)]
    return ' + '.join(texts)

def text_length(soup):
    return funcToCode(soup, 'len', 'VALUE')

def text_charAt(soup):
    return valueToCode(soup, 'VALUE') + '[' + \
            valueToCode(soup, 'AT') + ' - 1 ]'

def text_fromOther(soup):
    return funcToCode(soup, 'unicode', 'TEXT')

def text_include(soup):
    return 'str({0}) in str({1})'.format(valueToCode(soup, 'VALUE'),
                                        valueToCode(soup, 'FIND'))
