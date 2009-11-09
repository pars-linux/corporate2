#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "essential-%s" % get.srcVERSION().split("_", 1)[1]
NoStrip = "/"
dest = "essential"

def install():
    shelltools.chmod("*", mode = 0644)
    pisitools.dodir("/usr/lib/%s" % dest)
    pisitools.insinto("/usr/lib/%s" % dest, "*")
