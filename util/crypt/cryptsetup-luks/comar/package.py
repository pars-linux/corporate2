#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

CRYPTTAB = """\
# <target name>     <source device>     <key file>  <options>
#
"""

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # Generate empty cryttab file for the first time
    if not os.path.exists(CRYPTTAB):
        open(CRYPTTAB, "w").write(CRYPTTAB)

