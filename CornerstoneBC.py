#!/usr/bin/python
#
#

from AppKit import NSWorkspace
import sys
import os

os.system('/usr/local/bin/bcomp "%s" "%s" ' % (sys.argv[1], sys.argv[3]))
