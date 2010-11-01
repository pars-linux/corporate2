#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())
KeepSpecial=["libtool"]

def setup():
    # Fix ffmpeg build error
    shelltools.export("CXXFLAGS", "%s -D__STDC_CONSTANT_MACROS" % get.CXXFLAGS())

    kde.configure("--with-libsamplerate \
                   --with-alsa \
                   --with-flac \
                   --with-libmad \
                   --with-vorbis \
                   --with-speex \
                   --without-jack \
                   --without-polypaudio")

def build():
    kde.make()

def install():
    kde.install()

    pisitools.dodoc("AUTHORS", "NEWS", "README")
