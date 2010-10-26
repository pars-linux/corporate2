#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) TUBITAK / UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

KeepSpecial = ["libtool"]

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --enable-python \
                         --with-html-dir=/%s/%s/html"
                         % (get.docDIR(), get.srcNAME()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/lib/*.la")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
