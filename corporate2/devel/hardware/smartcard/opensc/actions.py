#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --enable-nsplugin \
                         --enable-openct \
                         --enable-pcsc \
                         --with-pinentry=/usr/bin/pinentry \
                         --with-pcsc-provider=/usr/lib/libpcsclite.so.1 \
                         --with-plugindir=/usr/lib/nsbrowser/plugins/")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/share/doc/opensc")

    pisitools.insinto("/etc", "etc/opensc.conf")

    pisitools.dohtml("doc/html.out/*.html")
    pisitools.dodoc("README")
