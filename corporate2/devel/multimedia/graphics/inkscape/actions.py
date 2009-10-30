#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "inkscape-0.47pre3"

def setup():
    autotools.configure("--with-gnome-vfs \
                         --enable-lcms \
                         --enable-poppler-cairo \
                         --disable-dependency-tracking \
                         --with-python \
                         --with-perl \
                         --with-xft")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.remove("/usr/share/applications/inkscape.desktop")
    pisitools.dodoc("AUTHORS", "COPYING", "COPYING.LIB", "ChangeLog", "NEWS", "README")
