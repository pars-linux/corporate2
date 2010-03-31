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
    shelltools.export("CFLAGS","%s -fstack-protector-all" % get.CFLAGS())

    autotools.autoreconf("-fi")
    autotools.configure("--enable-user-local=no \
                         --disable-usr-local \
                         --disable-static \
                         --enable-gtk2 \
                         --enable-ipv6 \
                         --enable-zlib \
                         --with-adns \
                         --with-gnu-ld \
                         --with-krb5 \
                         --with-net-snmp \
                         --with-pcap \
                         --with-pcre \
                         --with-pic \
                         --with-ssl \
                         --enable-warnings-as-errors=no \
                         --without-portaudio \
                         --with-plugins=/usr/lib/wireshark/plugins")
                         # --disable-warnings-as-errors \



def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/icons/hicolor/48x48/apps", "image/hi48-app-wireshark.png", "wireshark.png")
    pisitools.insinto("/usr/share/applications/", "wireshark.desktop")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README*")
