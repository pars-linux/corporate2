#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "gecko-mediaplayer"

def setup():
    shelltools.export("AT_M4DIR", "m4")
    autotools.autoreconf("-vfi")

    autotools.configure("--disable-schemas-install")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    # installing schemas by hand since make install causes sandboxviolations
    pisitools.insinto("/etc/gconf/schemas/", "gecko-mediaplayer.schemas")

    pisitools.rename("/usr/lib/mozilla", "nsbrowser")
    pisitools.remove("/%s/%s/INSTALL" % (get.docDIR(), get.srcNAME()))

