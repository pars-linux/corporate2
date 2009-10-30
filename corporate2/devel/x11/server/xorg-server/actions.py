#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.chmod("hw/vnc/symlink-vnc.sh")

    autotools.autoreconf("-fiv")
    autotools.configure("--enable-install-libxf86config \
                         --enable-aiglx \
                         --enable-glx-tls \
                         --enable-composite \
                         --enable-record \
                         --enable-dri \
                         --enable-dri2 \
                         --enable-config-dbus \
                         --enable-config-hal \
                         --enable-xfree86-utils \
                         --enable-xorg \
                         --disable-xcliplist \
                         --enable-vnc \
                         --enable-dmx \
                         --enable-xvfb \
                         --disable-xnest \
                         --enable-kdrive \
                         --enable-xephyr \
                         --disable-xsdl \
                         --disable-xfake \
                         --disable-xfbdev \
                         --with-pic \
                         --with-int10=x86emu \
                         --with-os-name=\"Pardus\" \
                         --with-os-vendor=\"TÜBİTAK, UEKAE\" \
                         --with-builderstring=\"Package: %s\" \
                         --with-fontdir=/usr/share/fonts \
                         --with-default-font-path=catalogue:/etc/X11/fontpath.d,built-ins \
                         --with-xkb-output=/var/lib/xkb \
                         --with-dri-driver-path=/usr/lib/xorg/modules/dri \
                         --localstatedir=/var \
                         PCI_TXT_IDS_DIR=/usr/share/X11/pci \
                         " % get.srcTAG())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/share/X11/pci")

    pisitools.remove("/usr/lib/xorg/modules/*.la")
    pisitools.remove("/usr/lib/xorg/modules/*/*.la")

    pisitools.remove("/usr/lib/X11/Options")

    # Move glx and dri modules for dynamic switching
    pisitools.domove("/usr/lib/xorg/modules/extensions/libglx.so", "/usr/lib/xorg/std/extensions")
    pisitools.domove("/usr/lib/xorg/modules/extensions/libdri.so", "/usr/lib/xorg/std/extensions")
