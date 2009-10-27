#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("config.h", "^#define NTPDRIFTFILE.*$", '#define NTPDRIFTFILE "/var/lib/ntp/drift/ntp.drift"')
    pisitools.dosed("config.h", "^#define ENABLE_IPV4LL$", "#undef ENABLE_IPV4LL")

def build():
    autotools.make('CC="%s" CFLAGS="%s" LDFLAGS="%s"' % (get.CC(), get.CFLAGS(), get.LDFLAGS()))

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc ("README")
