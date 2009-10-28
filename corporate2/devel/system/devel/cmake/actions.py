#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

majorVersion = ".".join(get.srcVERSION().split(".")[:2])

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --system-libs \
                            --docdir=/share/doc/cmake \
                            --mandir=/share/man")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosed("%s/usr/share/man/man1/*" % get.installDIR(), get.curDIR(), "/usr/share/cmake-%s" % majorVersion)
    pisitools.dosed("%s/usr/share/doc/cmake/*" % get.installDIR(), get.curDIR(), "/usr/share/cmake-%s" % majorVersion)
