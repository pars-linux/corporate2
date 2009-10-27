#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pythonmodules.install()

    # Move PİSİ into /usr/lib/pisi so we can protect ourself from python updates
    pisitools.domove("/usr/lib/%s/site-packages/pisi/" % get.curPYTHON(), "/usr/lib/pardus/", "pisi")

    pisitools.dosym("/usr/bin/pisi-cli", "/usr/bin/pisi")
