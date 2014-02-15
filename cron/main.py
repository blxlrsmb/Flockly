#!/usr/bin/env python2.7
# coding: utf-8
import mongo
from user import User
from blockly import Blockly
import time
import os
import sys
import traceback
reload(sys)
sys.setdefaultencoding(sys.getfilesystemencoding())

MIN_GAP = 5
GENERATOR_PATH = "../compiler/generator.py"
PYTHON_CMD = "python2"


while True:
    try:
        for blo in Blockly.objects:
            try:
                lastexecution, timesexecuted = blo.lastexecution, blo.timesexecuted
                if time.time() - lastexecution < MIN_GAP:
                    continue
                f = open('/tmp/flockly.xml', 'wb')
                print blo.content
                f.write(blo.content)
                f.close()
                f = open('./flockly.py', 'wb')
                f.write("# coding: utf-8\nfrom fbapi import *\nimport sys\nreload(sys)\nsys.setdefaultencoding('utf-8')\nsys.tracebacklimit=0\nimport datetime\n")
                f.close()
                os.system("echo [SYSTEM] Generating code > /tmp/flockly.run.log")
                os.system(GENERATOR_PATH + " /tmp/flockly.xml >> ./flockly.py 2>>/tmp/flockly.run.log")
                os.system("echo [SYSTEM] Generated code: >> /tmp/flockly.run.log")
                os.system("cat ./flockly.py >> /tmp/flockly.run.log")
                os.system("echo [SYSTEM] Running >> /tmp/flockly.run.log")
                os.system(PYTHON_CMD + " ./flockly.py " + blo.userid + " " + str(blo.id)  + " 1>>/tmp/flockly.run.log 2>&1")
                os.unlink('./flockly.py')
                blo.lastexecution = int(time.time())
                blo.timesexecuted = blo.timesexecuted + 1
                blo.logs.append(open('/tmp/flockly.run.log', 'rb').read(1024))
                if len(blo.logs) > 5:
                    blo.logs = blo.logs[-5:]
                blo.save()
            except Exception as e:
                print >>sys.stderr, e
                print >>sys.stderr, traceback.format_exc()
            finally:
                time.sleep(1)

    except Exception as e:
        print >>sys.stderr, e
        print >>sys.stderr, traceback.format_exc()
