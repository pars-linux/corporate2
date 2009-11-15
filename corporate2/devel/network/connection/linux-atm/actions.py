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

def setup():
    shelltools.export("CFLAGS", "%s -fno-strict-aliasing" % get.CFLAGS())
    pisitools.dosed("src/Makefile.in", "br2684", "")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s man_prefix=/usr/share/man" % get.installDIR())
    pisitools.insinto("/etc", "src/config/hosts.atm")

    pisitools.dodoc("AUTHORS", "THANKS", "ChangeLog", "BUGS", "NEWS", "README")
