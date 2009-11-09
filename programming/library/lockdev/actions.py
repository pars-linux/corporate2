#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # disable tests
    pisitools.dosed("Makefile", "^.*cd LockDev && make test$", "")

    # Set CFLAGS
    pisitools.dosed("Makefile", "OPTIMIZE=\".*\"", "OPTIMIZE=\"%s\"" % get.CFLAGS())

def build():
    autotools.make("CC=%s CFLAGS=\"%s -fPIC\"" % (get.CC(), get.CFLAGS()))

def install():
    autotools.rawInstall("sbindir=%s/sbin \
                          libdir=%s/usr/lib \
                          incdir=%s/usr/include \
                          mandir=%s/usr/share/man" % ((get.installDIR(),)*4))

    pisitools.remove("/usr/lib/*.a")

    pisitools.dosym("liblockdev.so.1.0.3", "/usr/lib/liblockdev.so.1")

    pisitools.dodoc("ChangeLog", "AUTHORS", "LICENSE")
