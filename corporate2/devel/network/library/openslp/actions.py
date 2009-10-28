#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS","%s -fPIC" % get.CFLAGS())

    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --disable-dependency-tracking \
                         --enable-slpv1 \
                         --enable-async-api \
                         --enable-slpv2-security")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/doc")

    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("AUTHORS", "FAQ", "ChangeLog", "NEWS", "README*", "THANKS")
