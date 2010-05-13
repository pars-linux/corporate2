#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-docdir=/usr/share/doc/%s \
                         --without-fltk" % get.srcNAME())

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("BUILDROOT=%s" % get.installDIR())

    pisitools.dodoc("CREDITS.txt", "LICENSE.txt", "CHANGES.txt")
