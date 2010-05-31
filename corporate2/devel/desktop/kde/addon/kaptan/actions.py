#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

shelltools.export('HOME', get.workDIR())

def install():

    pythonmodules.install()

    pythonmodules.fixCompiledPy("/usr/kde/3.5/share/apps/kaptan")

    pisitools.remove("%s/bin/kaptan" % get.kdeDIR())
    pisitools.dosym("%s/share/apps/kaptan/kaptan.py" % get.kdeDIR(), "%s/bin/kaptan" % get.kdeDIR())

    pisitools.removeDir("/usr/share")
