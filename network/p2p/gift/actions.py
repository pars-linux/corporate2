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
    autotools.configure("--enable-libmagic \
                         --enable-libogg \
                         --enable-libvorbis")

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/include/libgift")
    pisitools.dodir("/usr/share/giFT")

    shelltools.touch("%s/usr/share/giFT/giftd.log" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "HACKING", "QUICKSTART", "README", "TODO")
