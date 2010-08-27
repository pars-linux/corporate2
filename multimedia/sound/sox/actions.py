#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS","%s -fsigned-char" % get.CFLAGS())

    #autotools.autoreconf("-fi")

    autotools.configure("--disable-static \
                         --disable-largefile \
                         --disable-dependency-tracking \
                         --enable-alsa \
                         --enable-libao \
                         --enable-oss \
                         --with-sndfile \
                         --with-ogg \
                         --with-flac \
                         --with-ffmpeg \
                         --with-mad \
                         --with-id3tag \
                         --with-lame \
                         --with-samplerate \
                         --with-ladspa")

    # autoreconf fails, lets fix the internal libtool file for correct as-needed usage
    replace = (r"(\\\$deplibs) (\\\$compiler_flags)", r"\2 \1")
    pisitools.dosed("libtool", *replace)

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("ChangeLog", "README", "NEWS", "AUTHORS", "COPYING", "LICENSE*")
