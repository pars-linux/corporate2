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
    autotools.autoreconf("-fi")
    autotools.configure("--enable-ipv6 \
                         --with-ssl \
                         --without-smi \
                         --enable-ipv6 \
                         --disable-smb \
                         --mandir=/usr/share/man")

def build():
    autotools.make('CCOPT="%s"' % get.CFLAGS())

def install():
    pisitools.dosbin("tcpdump")

    pisitools.doman("tcpdump.1")
    pisitools.dodoc("CHANGES", "LICENSE", "README", "CREDITS", "*.awk")
