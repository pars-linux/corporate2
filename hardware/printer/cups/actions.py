#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("DSOFLAGS", get.LDFLAGS())
    shelltools.export("CFLAGS", "%s -DLDAP_DEPRECATED" % get.CFLAGS())

    # FIXME: pnp, pnpadmin -> lp, lpadmin
    # pdftops from cups is currently overridden by our additional file

    # For --enable-avahi
    autotools.aclocal("-I config-scripts")
    autotools.autoconf("-I config-scripts")

    autotools.configure('--with-cups-user=pnp \
                         --with-cups-group=pnp \
                         --with-system-groups=pnpadmin \
                         --with-docdir=/usr/share/cups/html \
                         --with-dbusdir=/etc/dbus-1 \
                         --localstatedir=/var \
                         --enable-slp \
                         --enable-acl \
                         --enable-libpaper \
                         --enable-debug \
                         --enable-avahi \
                         --enable-ssl \
                         --enable-gnutls \
                         --enable-threads \
                         --enable-gssapi \
                         --enable-dbus \
                         --enable-pam \
                         --enable-png \
                         --enable-jpeg \
                         --enable-tiff \
                         --enable-pie \
                         --enable-relro \
                         --enable-dnssd \
                         --enable-browsing \
                         --enable-ldap \
                         --disable-openssl \
                         --disable-launchd \
                         --without-rcdir \
                         --with-pdftops=pdftops \
                         --with-optim="%s -fstack-protector-all" \
                         --without-php' % get.CFLAGS())

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("BUILDROOT=%s" % get.installDIR())

    pisitools.dodir("/usr/share/cups/profiles")
    pisitools.dodir("/usr/libexec/cups/driver")
    pisitools.dodir("/var/log/cups")
    pisitools.dodir("/var/run/cups/certs")
    pisitools.dodir("/var/cache/cups")
    pisitools.dodir("/var/spool/cups/tmp")

    # cleanups
    pisitools.removeDir("/etc/pam.d")

    # Serial backend needs to run as root
    shelltools.chmod("%s/usr/lib/cups/backend/serial" % get.installDIR(), 0700)

    pisitools.dodoc("CHANGES.txt", "CREDITS.txt", "LICENSE.txt", "README.txt")
