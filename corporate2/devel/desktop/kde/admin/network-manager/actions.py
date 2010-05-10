#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export('HOME', get.workDIR())
KeepSpecial=["libtool"]

def install():
    pythonmodules.install()
    binpath = "%s/bin/network-manager" % get.kdeDIR()
    pisitools.remove(binpath)
    pisitools.dosym("%s/share/apps/network-manager/network-manager.py" % get.kdeDIR(), binpath)
    binpath = "%s/bin/network-applet" % get.kdeDIR()
    pisitools.remove(binpath)
    pisitools.dosym("%s/share/apps/network-manager/network-applet.py" % get.kdeDIR(), binpath)
