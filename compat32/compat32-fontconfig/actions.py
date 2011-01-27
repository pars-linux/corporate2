# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
shelltools.export("CXXFLAGS", "%s -m32" % get.CXXFLAGS())
shelltools.export("PKG_CONFIG_LIBDIR", "/usr/lib32/pkgconfig")

def setup():
    # Do not rebuild docs
    shelltools.export("HASDOCBOOK", "no")

    autotools.autoreconf("-vif")
    autotools.configure("--disable-static \
                         --disable-docs \
                         --x-includes=/usr/include \
                         --x-libraries=/usr/lib32 \
                         --libdir=/usr/lib32 \
                         --with-cache-dir=/var/cache/fontconfig \
                         --with-default-fonts=/usr/share/fonts \
                         --with-add-fonts=/usr/local/share/fonts")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for _dir in ("/usr/share", "/usr/include", "/usr/bin", "/etc", "/var"):
        pisitools.removeDir(_dir)

