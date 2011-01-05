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
    autotools.configure("--with-python \
                         --with-perl \
                         --include=/usr/include \
                         --with-tcl \
                         --with-krb5 \
                         --with-gssapi \
                         --with-ldap \
                         --with-openssl \
                         --with-pam \
                         --disable-rpath \
                         --enable-thread-safety \
                         --enable-nls \
                         --enable-integer-datetimes \
                         --enable-thread-safety \
                         --host=%s \
                         --datadir=/usr/share/pgsql \
                         --libdir=/usr/lib \
                         --with-docdir=/usr/share/doc/pgsql" % get.CHOST())

def build():
    if get.LDFLAGS():
        ld = "-j1 LD=%s %s" % (get.LD(), get.LDFLAGS())
    else:
        ld = "-j1 LD=%s" % get.LD()

    autotools.make("%s world" % ld)

def install():
    autotools.rawInstall("DESTDIR=%s LIBDIR=%s/usr/lib install-world" % (get.installDIR(), get.installDIR()))

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    pisitools.dodir("/var/lib/pgsql")
    pisitools.dodir("/var/lib/pgsql/data")
    pisitools.dodir("/var/lib/pgsql/backups")

    pisitools.dodoc("README", "HISTORY", "COPYRIGHT", "doc/README.*", "doc/TODO", "doc/bug.template")
