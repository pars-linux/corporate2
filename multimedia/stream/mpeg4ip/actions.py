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

import os

docdir = "%s/%s" % (get.docDIR(), get.srcNAME())

def removeWerror(d):
    for root, dirs, files in os.walk(d):
        for name in files:
            if name.startswith("Makefile") or name.startswith("configure"):
                pisitools.dosed(os.path.join(root, name), "-Werror", "-Wall")
                pisitools.dosed(os.path.join(root, name), "-Wmissing-prototypes", "-Wall")

def setup():
    removeWerror("./")
    shelltools.export("CFLAGS", "%s -fno-strict-aliasing -Wno-error" % get.CFLAGS())
    shelltools.export("LDFLAGS", get.LDFLAGS().replace("-Wl,--as-needed", ""))

    # autotools.autoreconf("-fi")
    shelltools.system("./bootstrap --prefix=/usr \
                       --host=%s \
                       --mandir=/usr/share/man \
                       --infodir=/usr/share/info \
                       --sysconfdir=/etc \
                       --libdir=/usr/lib \
                       --localstatedir=/var/lib \
                       --disable-warns-as-err \
                       --enable-server \
                       --datadir=/usr/share/mpeg4ip \
                       --enable-a52dec \
                       --enable-alsa \
                       --enable-faac \
                       --enable-ffmpeg \
                       --enable-gtk-glib \
                       --enable-id3tags \
                       --enable-ipv6 \
                       --enable-mmx \
                       --enable-mp3lame \
                       --enable-mp4live \
                       --enable-mpeg2dec \
                       --enable-player \
                       --enable-v4l2 \
                       --enable-x264 \
                       --enable-xvid \
                       --disable-arts \
                       --disable-srtp \
                       --disable-ppc \
                       --disable-static \
                       --disable-esd \
                       --disable-nas" % get.CHOST())

def build():
    pisitools.dosed("common/video/iso-mpeg4/src/Makefile", "-Werror")
    pisitools.dosed("lib/mpeg2ps/Makefile", "-Wl,--as-needed")

    for i in ["", ".am", ".in"]:
        pisitools.dosed("common/video/iso-mpeg4/src/Makefile%s" % i, "-Wmissing-prototypes")

    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("doc/MPEG4IP_Guide.pdf", "doc/*txt", "AUTHORS", "TODO")
    pisitools.dohtml("doc/*.html", "FEATURES.html")

    for f in shelltools.ls("doc/ietf/*.txt"):
        pisitools.insinto("%s/ietf/" % docdir, f)

    for f in shelltools.ls("doc/mcast/*"):
        if not "Makefile" in f:
            pisitools.insinto("%s/mcast/" % docdir, f)

    # these come from libmp4v2
    pisitools.remove("/usr/include/mp4.h")

    for f in shelltools.ls("%s/usr/lib/libmp4v2*" % get.installDIR()):
        shelltools.unlink(f)
