#!/usr/bin/env python
# -*- coding=UTF-8 -*-


import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

from generators.common import *


def math_arithmetic(soup):
    ops = {
          'ADD': ' + ',
          'MINUS': ' - ',
          'MULTIPLY': ' * ',
          'DIVIDE': ' / ',
          'POWER': ' ** '
          }
    ret = "int({})".format(valueToCode(soup, 'A'))
    ret += ops[findName(soup, 'OP').text]
    ret += "int({})".format(valueToCode(soup, 'B'))
    return ret


def math_number(soup):
    return repr(int(findName(soup, 'NUM').text))


def math_change(soup):
    return findName(soup, 'VAR').text + \
                    ' += ' + valueToCode(soup, 'DELTA')

def math_single(soup):
    ops = {
            'ABS': 'abs',
            'ROOT': 'math.sqrt'
            }
    return funcToCode(soup, \
            ops[findName(soup, 'NUM')['label']], 'NUM')

def math_modulo(soup):
    return valueToCode(soup, 'DIVIDEND') + ' % ' + \
            valueToCode(soup, 'DIVISOR')


def math_random_int(soup):
    return funcToCode(soup, 'random.randint', 'FROM', 'TO')
