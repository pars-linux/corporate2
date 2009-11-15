#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make('COPTS="%s -fPIC"' % get.CFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s/usr INSTROOT=%s install-etcppp" % (get.installDIR(),get.installDIR()))

    # No suid libraries
    shelltools.chmod("%s/usr/lib/pppd/%s/*.so" % (get.installDIR(),get.srcVERSION()), 0755)

    # Install Radius config files
    pisitools.insinto("/etc/radiusclient","pppd/plugins/radius/etc/*")

    pisitools.dodoc("Changes*","README*","FAQ")
