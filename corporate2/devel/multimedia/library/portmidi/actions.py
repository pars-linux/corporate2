#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "portmidi"

def build():
    pisitools.dosed("pm_linux/Makefile", "gcc", get.CC())
    pisitools.dosed("pm_linux/Makefile", "\-o pm_test\/", "-o pm_test\/portmidi-")

    autotools.make("-j1 -f pm_linux/Makefile \
                    CFLAGS=\"%s -fPIC\" \
                    VERSION=\".%s\"" % (get.CFLAGS(), get.srcVERSION()))

def install():
    autotools.make("-f pm_linux/Makefile install \
                    DESTDIR=%s \
                    LIBDIR=/usr/lib \
                    INCLUDEDIR=/usr/include" % get.installDIR())

    pisitools.insinto("/usr/include", "pm_common/pmutil.h")

    # Install test applications
    for app in ["latency", "midithread", "midithru", "mm", "qtest", "sysex", "test"]:
        pisitools.dobin("pm_test/portmidi-%s" % app)

    pisitools.dodoc("CHANGELOG.txt", "license.txt", "README.txt")
