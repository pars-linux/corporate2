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

WorkDir="dhcp-%s" % get.srcVERSION()

def setup():
    shelltools.export("CFLAGS", "%s -D_GNU_SOURCE" % get.CFLAGS())
    pisitools.dosed("client/scripts/linux", "/etc/dhclient-exit-hooks", "/etc/dhcp/dhclient-exit-hooks")
    pisitools.dosed("client/scripts/linux", "/etc/dhclient-enter-hooks", "/etc/dhcp/dhclient-enter-hooks")

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/etc/dhcpd.conf")
    pisitools.remove("/etc/dhclient.conf")

    # Create directory hierarchy in /var
    pisitools.dodir("/var/run/dhcp")
    pisitools.dodir("/var/lib/dhcp")

    pisitools.dodoc("README", "RELNOTES")
