#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("src/osdep/unix/Makefile","SSLDIR=/usr/local/ssl","SSLDIR=/usr/")
    pisitools.dosed("src/osdep/unix/Makefile","SSLCERTS=$(SSLDIR)/certs","SSLCERTS=/etc/pki/tls/certs/")

def build():
    autotools.make("lnp EXTRAAUTHENTICATORS=gss SSLTYPE=unix.nopwd  \
            EXTRACFLAGS=\"%s\" " %get.CFLAGS())

def install():
    pisitools.dolib("c-client/libc-client.so.1.0.0")
    pisitools.dosym("/usr/lib/libc-client.so.1.0.0", "/usr/lib/libc-client.so.1")
    pisitools.dosym("libc-client.so.1.0.0","/usr/lib/libc-client.so")
    pisitools.dodir("/usr/include/imap")
    pisitools.insinto("/usr/include/imap", "c-client/*.h")
    pisitools.insinto("/usr/include/imap", "c-client/linkage.c")
    pisitools.remove("/usr/include/imap/os_*.h")
