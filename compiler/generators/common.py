#!/usr/bin/env python
# -*- coding=UTF-8 -*-


import sys
import uuid
from ..generator import blockToCode

if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

findName = lambda soup, name: soup.findChild(attrs={'name': name})

indentCode = lambda s: '\n'.join(
    ['  '+i for i in s.split('\n')])

valueToCode = lambda soup, name: '(' + \
    blockToCode(findName(soup, name).block) + ')'

def funcToCode(soup, func, *var):
    params = []
    for i in var:
        if isinstance(i, str):
            params.append(valueToCode(soup, i))
        else:  # tuple
            _tmp = findName(soup, i[0]).text
            if i[1] == int:
                _tmp = int(_tmp)
            _tmp = repr(_tmp)
            params.append(_tmp)
    return func + '(' + ', '.join(params) + ')'
