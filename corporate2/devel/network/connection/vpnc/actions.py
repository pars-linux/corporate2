#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make('CFLAGS="%s -fPIE" LDFLAGS="%s -pie -lgcrypt"' % (get.CFLAGS(),get.LDFLAGS()))

def install():
    # bins.
    pisitools.dobin("vpnc")
    pisitools.dobin("vpnc-disconnect")
    pisitools.dobin("pcf2vpnc")
    pisitools.doexe("vpnc-script", "/etc/vpnc")

    # docs.
    pisitools.dodoc("README")
    pisitools.doman("vpnc.8")

    # conf.
    pisitools.insinto("/etc", "vpnc.conf")
