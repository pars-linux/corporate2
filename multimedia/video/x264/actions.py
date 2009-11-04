#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="x264-snapshot-%s-2245" % get.srcVERSION().split("_")[1]

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --enable-pthread \
                            --enable-shared \
                            --enable-pic \
                            --enable-mp4-output")

def build():
    autotools.make()

def install():
    autotools.install()

    # No static libs
    pisitools.remove("/usr/lib/libx264.a")
