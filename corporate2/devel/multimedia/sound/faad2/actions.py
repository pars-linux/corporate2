#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "faad2"

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--with-mp4v2 \
                         --without-xmms \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dosed("%s/usr/include/mp4ff.h" % get.installDIR(), '"mp4ff_int_types.h"', '<stdint.h>')

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "README.linux", "TODO")
