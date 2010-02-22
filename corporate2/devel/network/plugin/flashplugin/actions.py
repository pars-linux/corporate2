#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = get.ARCH()
NoStrip = "/"

def install():
    pisitools.doexe("libflashplayer.so", "/opt/netscape/plugins")
    pisitools.dodir("/usr/lib/nsbrowser/plugins")
    pisitools.dosym("/opt/netscape/plugins/libflashplayer.so", "/usr/lib/nsbrowser/plugins/libflashplayer.so")
