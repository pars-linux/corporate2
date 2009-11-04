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

WorkDir="libcaca-%s" % get.srcVERSION().replace("_",".")

def setup():
    autotools.autoreconf("-fi")
    libtools.libtoolize("--force --install")
    autotools.configure("--disable-doc \
                         --disable-static \
                         --disable-ruby \
                         --disable-csharp \
                         --enable-ncurses \
                         --enable-slang \
                         --enable-imlib2 \
                         --enable-x11 \
                         --with-x \
                         --x-libraries=/usr/lib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "ChangeLog", "NEWS","NOTES", "README", "THANKS")
