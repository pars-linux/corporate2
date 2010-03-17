#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "pkinit-nss-%s-1" % get.srcVERSION()

def setup():
    # Fix includes
    pisitools.dosed("src/pkinit.h", "<nss3/(.*)>", "<nss/\\1>")

    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --enable-gcc-warnings \
                         --with-default-server-nss-dbdir=/var/lib/kerberos/krb5kdc/ \
                         --with-default-client-nss-dbdir=/etc/ssl/nssdb")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodoc("NEWS", "ChangeLog", "COPYING")
