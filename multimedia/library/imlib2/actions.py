#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --enable-visibility-hiding \
                         --with-x \
                         --with-jpeg \
                         --with-png \
                         --with-tiff \
                         --with-gif \
                         --with-zlib \
                         --with-bzip2 \
                         --with-id3 \
                         --disable-amd64 \
                         --enable-mmx")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc/*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO")
