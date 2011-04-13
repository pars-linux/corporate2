#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

# enable loader builds DLL loader for ELF i386 platforms only
dllloader = "" if get.ARCH() == "x86_64" else "--enable-loader"

def setup():
    # Make it build with libtool 1.5
    shelltools.system("rm -rf m4/lt* m4/libtool.m4")

    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-a52 \
                         --enable-aa \
                         --enable-alsa \
                         --enable-dca \
                         --enable-dvb \
                         --enable-dvbpsi \
                         --enable-dvdnav \
                         --enable-dvdread \
                         --enable-faad \
                         --enable-flac \
                         --enable-freetype \
                         --enable-fribidi \
                         --enable-glx \
                         --enable-gnutls \
                         --enable-id3tag \
                         --enable-libcddb \
                         --enable-libmpeg2 \
                         --enable-libxml2 \
                         --enable-lirc \
                         --enable-live555 \
                         --enable-lua \
                         --enable-mad \
                         --enable-mkv \
                         --enable-mod \
                         --enable-mozilla \
                         --enable-mpc \
                         --enable-ogg \
                         --enable-opengl \
                         --enable-png \
                         --enable-pulse \
                         --enable-qt4 \
                         --enable-realrtsp \
                         --enable-screen \
                         --enable-sdl \
                         --enable-shared \
                         --enable-skins2 \
                         --enable-smb \
                         --enable-sout \
                         --enable-speex \
                         --enable-svg \
                         --enable-theora \
                         --enable-twolame \
                         --enable-upnp \
                         --enable-v4l \
                         --enable-vcd \
                         --enable-vcdx \
                         --enable-vlm \
                         --enable-vorbis \
                         --disable-altivec \
                         --disable-bonjour \
                         --disable-gnomevfs \
                         --disable-growl \
                         --disable-jack \
                         --disable-portaudio \
                         --disable-snapshot \
                         --disable-static %s " % dllloader )

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for icon in ("128x128", "48x48", "32x32", "16x16"):
        pisitools.insinto("/usr/share/icons/hicolor/%s/apps/" % icon, "share/icons/%s/vlc*.png" % icon)

    # Fix Firefox plugin location
    pisitools.rename("/usr/lib/mozilla","nsbrowser")
    pisitools.remove("/usr/lib/nsbrowser/plugins/*.la")

    # Remove kde4 related desktop files
    pisitools.removeDir("/usr/share/kde4")

    pisitools.dodoc("AUTHORS", "THANKS", "NEWS", "README", "HACKING", "doc/fortunes.txt", "doc/intf-vcd.txt")

