#!/usr/bin/env python2.7
# coding: utf-8
import mongo
from user import User
from blockly import Blockly
import time
import os
import sys
reload(sys)
sys.setdefaultencoding(sys.getfilesystemencoding())

MIN_GAP = 60
GENERATOR_PATH = "../generator/generate.py"
PYTHON_CMD = "python2"


while True:
    try:
        for blo in Blockly.objects:
            try:
                lastexecution, timesexecuted = blo.lastexecution, blo.timesexecuted
                if time.time() - lastexecution < MIN_GAP:
                    continue
                f = open('/tmp/flockly.xml', 'wb')
                f.write(blo.content)
                f.close()
                f = open('/tmp/flockly.py', 'wb')
                f.write('from fbapi import *')
                f.close()
                os.system(GENERATOR_PATH + " >> /tmp/flockly.py")
                os.system(PYTHON_CMD + " /tmp/flockly.py >/dev/null 2>/dev/null")
                blo.lastexecution = int(time.time())
                blo.timesexecuted = blo.timesexecuted + 1
                blo.save()
            except Exception as e:
                print >>sys.stderr, e

    except Exception as e:
        print >>sys.stderr, e
