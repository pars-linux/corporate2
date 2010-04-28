#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import kde
from pisi.actionsapi import get

KeepSpecial = ["libtool"]

def setup():
    autotools.autoconf("-f")
    kde.configure("--enable-libsuffix= \
                   --enable-ffmpeg-all-codecs \
                   --disable-rpath \
                   --disable-warnings \
                   --with-alsa \
                   --with-hal \
                   --with-lame \
                   --with-flac \
                   --with-libmad \
                   --with-oggvorbis \
                   --with-libdvdread \
                   --with-musepack \
                   --with-sndfile \
                   --with-musicbrainz \
                   --with-external-libsamplerate \
                   --without-resmgr \
                   --without-k3bsetup")

def build():
    kde.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "FAQ", "KNOWNBUGS", "PERMISSIONS", "README", "TODO")
