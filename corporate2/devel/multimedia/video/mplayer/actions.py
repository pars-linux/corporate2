#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

import os

WorkDir = "mplayer-%s" % get.srcVERSION().split("_", 1)[1]
mp_version = "29789"
ff_version = "20334"

def fixPermissions(dest):
    for root, dirs, files in os.walk(dest):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    fixPermissions("DOCS")
    shelltools.export("LINGUAS", "tr")

    shelltools.unlink("version.sh")
    shelltools.echo("version.sh", '#!/bin/bash\necho "#define VERSION \\\"dev-SVN-r%s\\\"" > version.h' % mp_version)
    shelltools.echo("version.sh", 'echo "#define MP_TITLE \\\"MPlayer dev-SVN-r%s (C) 2000-2009 MPlayer Team\\\" " >> version.h' % mp_version)
    shelltools.chmod("version.sh", 0755)

    shelltools.export("CFLAGS", "%s -O3 -ffast-math -fomit-frame-pointer" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -O3 -ffast-math -fomit-frame-pointer" % get.CXXFLAGS())

    autotools.rawConfigure('--prefix=/usr \
                            --confdir=/usr/share/mplayer \
                            --datadir=/usr/share/mplayer \
                            --disable-3dfx \
                            --disable-altivec \
                            --disable-arts \
                            --disable-bitmap-font \
                            --disable-debug \
                            --disable-dvdread-internal \
                            --disable-esd \
                            --disable-fribidi \
                            --disable-ggi \
                            --disable-libdvdcss-internal \
                            --disable-mga \
                            --disable-nas \
                            --disable-ssse3 \
                            --disable-svga \
                            --disable-tdfxfb \
                            --disable-tdfxvid \
                            --enable-aa \
                            --enable-alsa \
                            --enable-ass \
                            --enable-bl \
                            --enable-caca \
                            --enable-cdparanoia \
                            --enable-cmov \
                            --enable-dvb \
                            --enable-dvdnav \
                            --enable-dvdread \
                            --enable-fbdev \
                            --enable-freetype \
                            --enable-ftp \
                            --enable-gif \
                            --enable-gl \
                            --enable-gui \
                            --enable-inet6 \
                            --enable-jack \
                            --enable-joystick \
                            --enable-jpeg \
                            --enable-langinfo \
                            --enable-largefiles \
                            --enable-libcdio \
                            --enable-liblzo \
                            --enable-libopencore_amrnb \
                            --enable-libopencore_amrwb \
                            --enable-libvorbis \
                            --enable-lirc \
                            --enable-mad \
                            --enable-mencoder \
                            --enable-menu \
                            --enable-mmx \
                            --enable-mmxext \
                            --enable-network \
                            --enable-openal \
                            --enable-ossaudio \
                            --enable-png \
                            --enable-pulse \
                            --enable-radio \
                            --enable-radio-capture \
                            --enable-radio-v4l2 \
                            --enable-real \
                            --enable-rtc \
                            --enable-runtime-cpudetection \
                            --enable-sdl \
                            --enable-shm \
                            --enable-smb \
                            --enable-sse \
                            --enable-tga \
                            --enable-tv \
                            --enable-tv-teletext \
                            --enable-tv-v4l1 \
                            --enable-tv-v4l2 \
                            --enable-unrarexec \
                            --enable-v4l2 \
                            --enable-v4lw \
                            --enable-vdpau \
                            --enable-win32dll \
                            --enable-x11 \
                            --enable-xf86keysym \
                            --enable-xinerama \
                            --enable-xshape \
                            --enable-xv \
                            --enable-xvmc \
                            --with-xvmclib=XvMCW \
                            --language=tr \
                            --charset=UTF-8 \
                            --codecsdir=/usr/lib/%(esdir)s \
                            --win32codecsdir=/usr/lib/%(esdir)s \
                            --xanimcodecsdir=/usr/lib/%(esdir)s \
                            --realcodecsdir=/usr/lib/%(esdir)s \
                            --extra-libs="-lopenal -ljack" \
                            --disable-rpath' \
                            % {"esdir": "essential"})

                            # stuff that fail hede=yes check, but working with hede=auto
                            # --disable-faad-external \
                            # --enable-directfb \
                            # --enable-fontconfig \
                            # --enable-xvid \
                            # --enable-theora \

def build():
    autotools.make("-j1")

def install():
    autotools.install("prefix=%(D)s/usr \
                       BINDIR=%(D)s/usr/bin \
                       LIBDIR=%(D)s/usr/lib \
                       CONFDIR=%(D)s/usr/share/mplayer \
                       DATADIR=%(D)s/usr/share/mplayer \
                       MANDIR=%(D)s/usr/share/man" % {"D": get.installDIR()})

    # set the default skin for gui
    shelltools.copytree("default_skin", "%s/usr/share/mplayer/skins/default" % get.installDIR())

    # codecs conf, not something user will interact with
    pisitools.insinto("/usr/share/mplayer", "etc/codecs.conf")

    # example dvb conf
    pisitools.insinto("/usr/share/mplayer", "etc/dvb-menu.conf")

    # just for fast access to conf
    pisitools.dosym("/etc/mplayer.conf", "/usr/share/mplayer/mplayer.conf")
    pisitools.dosym("/etc/mencoder.conf", "/usr/share/mplayer/mencoder.conf")

    # install docs, tools, examples
    pisitools.dodoc("AUTHORS", "Changelog", "README", "LICENSE")
    pisitools.insinto("/%s/%s/" % (get.docDIR(), get.srcNAME()), "TOOLS")
    pisitools.insinto("/%s/%s/" % (get.docDIR(), get.srcNAME()), "DOCS/tech")
    pythonmodules.fixCompiledPy("/usr/share/doc")

    # we will use our own desktop file and icon
    pisitools.remove("/usr/share/applications/mplayer.desktop")
    pisitools.remove("/usr/share/pixmaps/mplayer.xpm")

