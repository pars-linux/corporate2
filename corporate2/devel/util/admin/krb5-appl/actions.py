#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    for manpage in open("manpaths.txt", "r").readlines():
        shelltools.move(manpage.strip(), "%s.in" % manpage.strip())

    autotools.autoheader()
    autotools.autoconf()

    shelltools.export("CFLAGS", "%s -I/usr/include/et -fPIE -fno-strict-aliasing" % get.CFLAGS())
    shelltools.export("LDFLAGS", "%s -pie" % get.LDFLAGS())

    autotools.configure("--with-pam")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Add "k" prefix to some apps and manpages to resolve conflicts
    for app in ["telnetd", "ftpd"]:
        pisitools.rename("/usr/share/man/man8/%s.8" % app, "k%s.8" % app)
        pisitools.rename("/usr/sbin/%s" % app, "k%s" % app)

    for app in ["rcp", "rsh", "telnet", "ftp", "rlogin"]:
        pisitools.rename("/usr/share/man/man1/%s.1" % app, "k%s.1" % app)
        pisitools.rename("/usr/bin/%s" % app, "k%s" % app)

    pisitools.remove("/usr/share/man/man1/tmac.doc")

    pisitools.dodoc("NOTICE", "README")
