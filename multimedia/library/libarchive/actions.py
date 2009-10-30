#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import libtools

def setup():
    libtools.libtoolize()
    autotools.aclocal()
    autotools.configure("--disable-static \
                         --disable-bsdtar \
                         --bindir=/bin ")
def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/share/man/man5/tar.5")
    pisitools.remove("/usr/share/man/man5/cpio.5")

    pisitools.dodoc("COPYING","NEWS","README")
