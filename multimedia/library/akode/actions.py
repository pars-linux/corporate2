#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde

def setup():
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
