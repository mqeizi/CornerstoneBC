#!/usr/bin/python
#
# TextMate Launch and Compare script
# Copyright (c) Zennaware GmbH, 2012. All rights reserved.
#

from AppKit import NSWorkspace
import sys
import os

os.system('/usr/local/bin/bcomp "%s" "%s" ' % (sys.argv[1], sys.argv[3]))