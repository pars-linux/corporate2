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
    shelltools.export("CFLAGS", "%s -fPIC" % get.CFLAGS())

    autotools.configure("--with-saslauthd=/var/lib/sasl2 \
                         --with-pwcheck=/var/lib/sasl2 \
                         --with-configdir=/etc/sasl2 \
                         --with-plugindir=/usr/lib/sasl2 \
                         --with-dbpath=/etc/sasl2/sasldb2 \
                         --with-pam \
                         --with-ldap \
                         --with-openssl \
                         --with-dblib=gdbm \
                         --with-gss_impl=mit \
                         --with-devrandom=/dev/urandom \
                         --without-pgsql \
                         --without-mysql \
                         --enable-anon \
                         --enable-cram \
                         --enable-digest \
                         --enable-gssapi \
                         --enable-ldapdb \
                         --enable-login \
                         --enable-ntlm \
                         --enable-plain \
                         --disable-krb4 \
                         --disable-otp \
                         --disable-java \
                         --disable-sql \
                         --disable-static")

def build():
    autotools.make("-j1")
    shelltools.cd("saslauthd")
    autotools.make("testsaslauthd")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodir("/etc/sasl2")
    pisitools.dodir("/var/lib/sasl2")

    for doc in ["AUTHORS", "COPYING", "ChangeLog", "LDAP_SASLAUTHD", "NEWS", "README"]:
        pisitools.newdoc("saslauthd/%s" % doc, "saslauthd/%s" % doc)

    pisitools.dohtml("doc/*.html")
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README", "doc/TODO", "doc/*.txt")
