#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--with-homedir=/var/lib/gnarwl")

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/bin", "src/gnarwl")
    pisitools.insinto("/usr/sbin", "src/damnit")

    pisitools.insinto("/var/lib/gnarwl", "data/header.txt")
    pisitools.insinto("/var/lib/gnarwl", "data/footer.txt")
    pisitools.insinto("/var/lib/gnarwl", "data/badheaders.txt", "badheaders.db")
    pisitools.insinto("/var/lib/gnarwl", "data/blacklist.txt", "blacklist.db")

    pisitools.insinto("/etc", "data/gnarwl.cfg")

    pisitools.doman("doc/damnit.8", "doc/gnarwl.8")

    pisitools.dodoc("doc/AUTHORS", "doc/FAQ", "doc/example.ldif", "doc/HISTORY", "doc/ISPEnv2.schema", "doc/ISPEnv.schema", "doc/LICENSE", "doc/README", "doc/README.upgrade")
