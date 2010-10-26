#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    for fl in ["NEWS", "AUTHORS", "ChangeLog"]:
        shelltools.touch(fl)
    autotools.autoreconf("-fi -Im4")

    libtools.libtoolize("--force --install")
    autotools.configure("--disable-debugging \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("CHANGES", "COPYRIGHT", "CREDITS", "README", "TODO", "VERSION")
