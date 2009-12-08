#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
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

    pisitools.remove("%s/bin/package-manager" % get.kdeDIR())
    pisitools.remove("%s/bin/pm-install" % get.kdeDIR())
    pisitools.dosym("%s/share/apps/package-manager/package-manager.py" % get.kdeDIR(), "%s/bin/package-manager" % get.kdeDIR())
    pisitools.dosym("%s/share/apps/package-manager/pm-install.py" % get.kdeDIR(), "%s/bin/pm-install" % get.kdeDIR())
