#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --enable-ssl \
                            --enable-ipv6")

def build():
    autotools.make('CC="%s" LDFLAGS="%s"' % (get.CC(), get.LDFLAGS()))

def install():
    pisitools.dobin("ftp/ftp")

    pisitools.doman("ftp/ftp.1", "ftp/netrc.5")
    pisitools.dodoc("ChangeLog", "README", "BUGS")
