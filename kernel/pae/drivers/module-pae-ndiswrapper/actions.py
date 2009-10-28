#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "ndiswrapper-%s" % get.srcVERSION()
KDIR = kerneltools.getKernelVersion()

def build():
    for i in ["driver/Makefile", "Makefile"]:
        pisitools.dosed(i, "\$\(shell uname -r\)", KDIR)

    pisitools.dosed("driver/Makefile", "/misc", "/extra")
    autotools.make("-C /lib/modules/%s/build M=`pwd`" % KDIR)

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr")
    pisitools.removeDir("/sbin")
    pisitools.remove("/lib/modules/%s/modules.*" % KDIR)
