#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "sidplay-libs-%s" % get.srcVERSION()
KeepSpecial = ["libtool"]

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static")

    pisitools.dosed("libsidplay/libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/include/resid", "resid/*.h")

    # Dirty way to install docs
    for d in ("libsidplay", "libsidutils", "resid"):
        for f in ("AUTHORS", "ChangeLog", "COPYING", "TODO", "README"):
            pisitools.insinto("/usr/share/doc/%s/%s" % (get.srcNAME(), d), "%s/%s" % (d, f))
