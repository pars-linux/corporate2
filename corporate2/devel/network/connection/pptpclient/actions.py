#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="pptp-1.7.2"

def setup():
    pisitools.dosed("routing.c", "/bin/ip", "/sbin/ip")

def build():
    autotools.make("CC=%s CFLAGS='%s' DESTDIR=%s" % (get.CC(), get.CFLAGS(), get.installDIR()))

def install():
    autotools.install("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "DEVELOPERS",
        "NEWS", "README", "TODO", "USING")

