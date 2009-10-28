#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) TUBITAK / UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "smartcam"
NoStrip = ["/usr/share/smartcam"]

def build():
    shelltools.cd("src/app")
    shelltools.system("%s %s `pkg-config --cflags --libs gtk+-2.0 gthread-2.0` -lbluetooth smartcam.c -o smartcam" % (get.CC(), get.CFLAGS()))

    shelltools.cd("../driver")
    autotools.make("-C /lib/modules/%s/build M=`pwd`" % get.curKERNEL())

def install():
    shelltools.cd("src/app")
    pisitools.dobin("smartcam")
    pisitools.rename("/usr/bin/smartcam", "smartcam.bin")

    shelltools.cd("../driver")
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "*.ko")

    for file in ("*.jar", "*.SIS"):
        pisitools.insinto("/usr/share/smartcam/phone_files", "../../release/phone_files/%s" % file)

    pisitools.dodoc("../../COPYING", "../../ReadMe.txt")
