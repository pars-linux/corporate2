#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("LDFLAGS", "%s -Wl,-z,now" % get.LDFLAGS())

    shelltools.system("./autogen.sh")
    kde.configure("--disable-dependency-tracking \
                   --enable-maintainer-mode \
                   --disable-pinentry-gtk \
                   --disable-pinentry-gtk2 \
                   --enable-pinentry-qt \
                   --enable-pinentry-curses \
                   --enable-fallback-curses \
                   --infodir=/usr/share/info")

def build():
    kde.make()

def install():
    kde.install()

    pisitools.remove("/usr/share/info/dir")
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS")
