#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    for f in ["NEWS", "AUTHORS"]:
        shelltools.touch(f)

    autotools.autoreconf("-vif")
    autotools.configure("--enable-mime \
                         --enable-extras \
                         --enable-contrast")

    pisitools.dosed("Makefile", "/usr/lib/gimp/", "%s/usr/lib/gimp/" % get.installDIR())

def build():
    autotools.make("schemasdir=/etc/gconf/schemas")

def install():
    autotools.install("schemasdir=%s/etc/gconf/schemas" % get.installDIR())

    # Do not conflict with dcraw package
    pisitools.remove("/usr/bin/dcraw")

    pisitools.insinto("/usr/share/mime/packages", "ufraw-mime.xml")

    pisitools.dodoc("COPYING", "ChangeLog", "MANIFEST", "README")
