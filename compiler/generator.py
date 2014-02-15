#!/usr/bin/env python2
# -*- coding=UTF-8 -*-

from generators import *

if __name__ == '__main__':
    BASE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
    if BASE_PATH not in sys.path:
        sys.path.append(BASE_PATH)
    print translate(open(sys.argv[1]).read())
