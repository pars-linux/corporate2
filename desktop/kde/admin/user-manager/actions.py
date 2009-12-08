#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export('HOME', get.workDIR())
KeepSpecial=["libtool"]

def install():
    pythonmodules.install()
    binpath = "%s/bin/user-manager" % get.kdeDIR()
    pisitools.remove(binpath)
    pisitools.dosym("%s/share/apps/user-manager/user-manager.py" % get.kdeDIR(), binpath)
    pisitools.removeDir("/usr/share/doc")
