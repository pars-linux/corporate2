#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="dhcp-4.1.0p1"

def setup():
    pisitools.dosed("client/scripts/linux", "/etc/dhclient-exit-hooks", "/etc/dhcp/dhclient-exit-hooks")
    pisitools.dosed("client/scripts/linux", "/etc/dhclient-enter-hooks", "/etc/dhcp/dhclient-enter-hooks")

def build():
    shelltools.export("CFLAGS","%s -D_GNU_SOURCE" % get.CFLAGS())
    autotools.configure()
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/etc/dhcpd.conf")
    pisitools.remove("/etc/dhclient.conf")
    pisitools.dodir("/var/run")
    pisitools.dodir("/var/lib/dhcp")
    shelltools.touch("%s/var/lib/dhcp/dhcpd.leases" % get.installDIR())
    shelltools.touch("%s/var/lib/dhcp/dhcpd.leases~" % get.installDIR())
    shelltools.touch("%s/var/run/dhcpd.pid" % get.installDIR())
    pisitools.dodoc("README", "RELNOTES")
