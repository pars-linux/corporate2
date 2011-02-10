#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-COCHRANE" % get.srcDIR()

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # zarafa's libmapi conflicts with this
    pisitools.dosym("libmapi-openchange.so.0.9", "/usr/lib/libmapi-openchange.so.0")

    libs = ["libmapiadmin", "libmapiproxy", "libmapiserver", "libmapistore", "libocpf"]
    for i in libs:
        pisitools.dosym("%s.so.0.9" % i, "/usr/lib/%s.so.0" % i)

    pisitools.removeDir("/usr/modules")

    pisitools.dodoc("CHANGELOG", "ChangeLog", "COPYING", "README")
