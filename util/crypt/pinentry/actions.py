#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-dependency-tracking \
                         --disable-rpath \
                         --disable-pinentry-gtk \
                         --enable-pinentry-qt4 \
                         --enable-pinentry-curses \
                         --enable-pinentry-qt \
                         --infodir=/usr/share/info")

    # Modify binary names for Qt3 and Qt4
    pisitools.dosed("qt/Makefile.in", "pinentry-qt", "pinentry-qt3")
    pisitools.dosed("qt4/Makefile.in", "pinentry-qt4", "pinentry-qt")

    # Fix MOC files
    shelltools.cd("qt4")
    shelltools.system("moc-qt4 pinentrydialog.h > pinentrydialog.moc")
    shelltools.system("moc-qt4 qsecurelineedit.h > qsecurelineedit.moc")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dosym("pinentry-gtk-2", "/usr/bin/pinentry-gtk")
    pisitools.remove("/usr/bin/pinentry")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS")
