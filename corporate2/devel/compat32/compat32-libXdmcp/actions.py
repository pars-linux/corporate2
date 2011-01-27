# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
shelltools.export("PKG_CONFIG_LIBDIR", "/usr/lib32/pkgconfig")

# For xproto which is not arch dependent
shelltools.export("PKG_CONFIG_PATH", "/usr/lib/pkgconfig")

def setup():
    autotools.configure("--disable-static \
                         --libdir=/usr/lib32")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for _dir in ("/usr/include",):
        pisitools.removeDir(_dir)
