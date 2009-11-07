#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir="mplib-beta-%s/src/texk/web2c/mpdir" % get.srcVERSION()
KeepSpecial=["libtool"]

def setup():
    autotools.autoreconf("-fi")
    libtools.libtoolize("--copy --force")
    autotools.configure("--enable-lua \
                         --disable-static")

def build():
    autotools.make("KPSESRCDIR=/usr/include/kpathsea KPSELIB=-lkpathsea -j1")

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.domove("/usr/bin/mpost", "/usr/bin/", "mpost-%s" % get.srcNAME())

    pisitools.dodoc("../../../../CHANGES")

