#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def install():
    pisitools.insinto("/", "etc")
    pisitools.insinto("/", "usr")

    for pofile in shelltools.ls("po/*.po"):
        lang = shelltools.baseName(pofile)[:3]
        pisitools.domo(pofile, lang, "byobu.mo")

    pisitools.dodoc("AUTHORS", "README", "COPYING")

