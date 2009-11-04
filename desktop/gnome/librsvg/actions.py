#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--with-svgz \
                         --with-croco \
                         --disable-gnome-print \
                         --disable-mozilla-plugin \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.removeDir("/usr/lib/mozilla/plugins")

    pisitools.dodoc("COPYING", "AUTHORS", "ChangeLog", "README")
