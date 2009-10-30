#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--enable-shared \
                         --disable-static \
                         --enable-djbfft")

def build():
    autotools.make('CFLAGS="%s"' % get.CFLAGS())

def install():
    autotools.rawInstall('DESTDIR="%s" docdir=/usr/share/doc/%s/html' % (get.installDIR(), get.srcNAME()))

    pisitools.insinto("/usr/include/a52dec", "liba52/a52_internal.h")
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "doc/liba52.txt")
