#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

shelltools.export('HOME', get.workDIR())
KeepSpecial=["libtool"]

def install():
    pythonmodules.install()
    binpath = "%s/bin/boot-manager" % get.kdeDIR()
    pisitools.remove(binpath)
    pisitools.dosym("%s/share/apps/boot-manager/boot-manager.py" % get.kdeDIR(), binpath)
    pisitools.removeDir("/usr/share/doc/")
