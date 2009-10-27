#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --disable-policy-kit \
                         --enable-pam-module \
                         --localstatedir=/var \
                         --with-pid-file=/var/run/ConsoleKit/pid")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s/" % get.installDIR())

    pisitools.removeDir("/usr/lib/ConsoleKit/scripts/")

    pisitools.dodir("/var/run/ConsoleKit")
    # pam_console-compat
    pisitools.dodir("/var/run/console")

    pisitools.dodoc("AUTHORS","ChangeLog","README", "COPYING", "HACKING", "NEWS", "TODO")
