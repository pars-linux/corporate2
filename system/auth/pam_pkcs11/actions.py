#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -DLDAP_DEPRECATED -fno-strict-aliasing" % get.CFLAGS())
    autotools.autoreconf("-fi")
    autotools.configure("--disable-dependency-tracking \
                         --with-nss \
                         --with-ldap \
                         --enable-debug \
                         --without-docbook \
                         --disable-rpath")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Move pam module to /lib
    pisitools.domove("/usr/lib/security/pam_pkcs11.so", "/lib")

    # Create necessary directories
    pisitools.dodir("/etc/pam_pkcs11/cacerts")
    pisitools.dodir("/etc/pam_pkcs11/crls")

    # Install conf files
    for f in shelltools.ls("etc/*.conf.example"):
        pisitools.insinto("/etc/pam_pkcs11", f, shelltools.baseName(f).rstrip(".example"))

    pisitools.dodoc("NEWS", "README", "doc/README*")
    pisitools.dohtml("doc/api/*.html")
    pisitools.doman("doc/*.[18]")
