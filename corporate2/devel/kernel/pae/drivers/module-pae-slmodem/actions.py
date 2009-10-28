#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="slmodem-%s" % get.srcVERSION().replace("_", "-")

def setup():
    shelltools.export("CFLAGS", get.CFLAGS().replace("-D_FORTIFY_SOURCE=2", ""))
    shelltools.export("CXXFLAGS", get.CXXFLAGS().replace("-D_FORTIFY_SOURCE=2", ""))

    pisitools.dosed("drivers/Makefile", "SUBDIRS=\$(shell pwd)", "SUBDIRS=%s/drivers" % get.srcDIR())
    pisitools.dosed("drivers/Makefile", "SUBDIRS=", "M=")
    pisitools.dosed("drivers/Makefile", "\$\(shell uname -r\)", get.curKERNEL())
    pisitools.dosed("Makefile", "\$\(shell uname -r\)", get.curKERNEL())

def build():
    autotools.make("SUPPORT_ALSA=1 modem")
    autotools.make("KERNEL_DIR=/lib/modules/%s/build drivers" % get.curKERNEL())

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "drivers/*.ko")
    pisitools.insinto("/usr/sbin", "modem/modem_test", "slmodem_test")
    pisitools.dosbin("modem/slmodemd")
    pisitools.dodir("/var/lib/slmodem")

    pisitools.dodoc("Changes", "README")

