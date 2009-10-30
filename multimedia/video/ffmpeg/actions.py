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

WorkDir = "ffmpeg"
version = "20334"

def setup():
    shelltools.export("CFLAGS","%s -DRUNTIME_CPUDETECT -O3 -ffast-math -fomit-frame-pointer" % get.CFLAGS())
    pisitools.dosed("configure", "die_license_disabled nonfr.*")

    # to keep the source tarball small, write svn version by hand
    shelltools.unlink("version.sh")
    shelltools.echo("version.sh", '#!/bin/bash\necho "#define FFMPEG_VERSION  \\\"SVN-r%s\\\"" > version.h' % version)
    shelltools.chmod("version.sh", 0755)

    # CPU thing is just used for CMOV detection
    autotools.rawConfigure("--cpu=i686 \
                            --prefix=/usr \
                            --mandir=/usr/share/man \
                            --enable-runtime-cpudetect \
                            --enable-gpl \
                            --enable-version3 \
                            --enable-pthreads \
                            --enable-postproc \
                            --enable-x11grab \
                            --enable-libdc1394 \
                            --enable-libfaac \
                            --enable-libfaad \
                            --enable-libgsm \
                            --enable-libmp3lame \
                            --enable-libnut \
                            --enable-libopencore-amrnb \
                            --enable-libopencore-amrwb \
                            --enable-libschroedinger \
                            --enable-libspeex \
                            --enable-libtheora \
                            --enable-libvorbis \
                            --enable-libx264 \
                            --enable-libxvid \
                            --enable-ipv6 \
                            --enable-shared \
                            --enable-mmx \
                            --enable-mmx2 \
                            --enable-sse \
                            --enable-vdpau \
                            --enable-yasm \
                            --disable-stripping \
                            --disable-static \
                            --disable-debug")

                            # Not yet
                            # --enable-avfilter \
                            # --enable-avfilter-lavf \
                            # FIXME: this may be nice, or not
                            # --enable-hardcoded-tables \

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc","doc/ffserver.conf")

    pisitools.dodoc("Changelog", "README")
