#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

# WorkDir = "v4l-dvb-214c94aa62aa"
WorkDir = "uvcvideo-214c94aa62aa"
KDIR = kerneltools.getKernelVersion()

def build():
    # kerneltools.build("KERNELRELEASE=%s oldconfig" % KDIR)
    autotools.make("KERNELRELEASE=%s" % KDIR)

def install():
    pisitools.insinto("/lib/modules/%s/extra" % KDIR, "v4l/*.ko")

    pisitools.dodoc("COPYING", "README")
