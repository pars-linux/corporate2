#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

shelltools.export('HOME', get.workDIR())
def install():
    pythonmodules.install()
    binpath = "%s/bin/disk-manager" % get.kdeDIR()
    pisitools.remove(binpath)
    pisitools.dosym("%s/share/apps/disk-manager/disk-manager.py" % get.kdeDIR(), binpath)
