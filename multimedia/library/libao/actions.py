#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    libtools.libtoolize("--force --install")
    autotools.configure("--enable-alsa09 \
                         --enable-alsa09-mmap \
                         --disable-arts \
                         --disable-pulse \
                         --disable-esd \
                         --disable-nas \
                         --enable-shared \
                         --disable-static")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/share/doc")

    pisitools.dohtml("doc/*")
    pisitools.dodoc("AUTHORS", "CHANGES", "README", "TODO")
