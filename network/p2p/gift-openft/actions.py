#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "gift-openft-%s" % get.srcVERSION()

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s giftconfdir='/etc/giFT' \
                                     plugindir='/usr/lib/giFT' \
                                     datadir='/usr/share/giFT' \
                                     giftperldir='/usr/bin' \
                                     includedir='/usr/include/libgift'" % get.installDIR())

    pisitools.dodoc("README", "NEWS", "ChangeLog", "TODO")
