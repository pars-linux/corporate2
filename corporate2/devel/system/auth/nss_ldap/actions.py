#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS","%s -fPIC" % get.CFLAGS())

    # Change search bases to something generic instead of padl
    pisitools.dosed("ldap.conf", "dc=padl", "dc=example")

    autotools.autoreconf("-fi")
    autotools.configure("--with-ldap-lib=openldap \
                         --libdir=/lib \
                         --disable-dependency-tracking \
                         --enable-sasl \
                         --enable-rfc2307bis \
                         --enable-configurable-krb5-ccname-gssapi \
                         --enable-paged-results")

def build():
    autotools.make("-j1")

def install():
    pisitools.dodir("/etc")
    autotools.rawInstall("DESTDIR=%s libdir=/lib" % get.installDIR())

    # Move the nsswitch.conf tweaked for ldap stuff into the docs
    pisitools.domove("/etc/nsswitch.ldap", "/%s/%s" % (get.docDIR(), get.srcNAME()))

    pisitools.dodoc("ChangeLog", "ANNOUNCE", "NEWS", "README", "AUTHORS", "ldap.conf")
