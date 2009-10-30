#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="last.fm-%s" % get.srcVERSION()

def setup():
    # Last.fm murdered our beautiful translation, replace it
    shelltools.unlink("i18n/lastfm_tr.ts")
    shelltools.move("lastfm_tr.ts","i18n/lastfm_tr.ts")

    shelltools.system("qmake-qt4 LastFM.pro")

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/bin","bin/last.fm","lastfm")
    pisitools.insinto("/usr/lib/lastfm","bin/services/*")
    pisitools.insinto("/usr/share/lastfm","bin/data/*.png")
    pisitools.insinto("/usr/share/lastfm/","bin/data/buttons")
    pisitools.insinto("/usr/share/lastfm/icons","bin/data/icons/*.png")

    # Library stuff
    for lib in ["LastFmTools","Moose"]:
        pisitools.insinto("/usr/lib","bin/lib%s.so.1.0.0" % lib, "lib%s.so.1" % lib)

    # Translations
    shelltools.cd("i18n")
    shelltools.system("lrelease-qt4 *.ts")
    pisitools.insinto("/usr/share/lastfm/i18n","*.qm")
    shelltools.cd("..")

    # Docs
    pisitools.dodoc("ChangeLog","COPYING","README")
