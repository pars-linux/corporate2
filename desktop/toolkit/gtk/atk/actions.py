#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-gtk-doc")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.removeDir("/usr/share/gtk-doc")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
