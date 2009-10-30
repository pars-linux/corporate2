#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "mpeg4ip-%s" % get.srcVERSION()

srclib = "lib/mp4v2"
targetinc = "/usr/include/libmp4v2"

def setup():
    shelltools.touch("bootstrapped")
    autotools.configure("--disable-warns-as-err \
                         --disable-server \
                         --disable-player \
                         --disable-mp4live \
                         --disable-id3tags \
                         --disable-xvid \
                         --disable-a52dec \
                         --disable-mad \
                         --disable-mpeg2dec \
                         --disable-srtp \
                         --disable-mp3lame \
                         --disable-faac \
                         --disable-ffmpeg \
                         --disable-x264 \
                         --disable-static")

    pisitools.dosed("%s/Makefile" % srclib, "SUBDIRS = . test util", "SUBDIRS = .")

def build():
    shelltools.cd(srclib)
    autotools.make()

def install():
    pisitools.dodir(targetinc)

    shelltools.cd(srclib)
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("README", "INTERNALS", "API_CHANGES", "TODO")

    shelltools.cd("../..")
    for f in ["include/mpeg4ip_version.h", "include/mpeg4ip.h", "mpeg4ip_config.h"]:
        pisitools.insinto(targetinc, f)

    pisitools.dosed("%s/usr/include/mp4.h" % get.installDIR(), '"mpeg4ip.h"', '<libmp4v2/mpeg4ip.h>')
    pisitools.dosed("%s/%s/mpeg4ip.h" % (get.installDIR(), targetinc), "mpeg4ip_config.h", "libmp4v2/mpeg4ip_config.h")
    pisitools.dosed("%s/%s/mpeg4ip.h" % (get.installDIR(), targetinc), '"mpeg4ip_version.h"', '<libmp4v2/mpeg4ip_version.h>')
    pisitools.dosed("%s/%s/mpeg4ip.h" % (get.installDIR(), targetinc), "#include <systems.h>", "#include <sys/types.h>")

