#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

x11docdir = "/%s/%s" % (get.docDIR(), get.srcNAME())

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--enable-txt \
                         --enable-pdf \
                         --disable-ps \
                         --disable-html \
                         --with-x11docdir=%s" % x11docdir)

def build():
    shelltools.export("HOME", get.curDIR())
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove Xprint related docs
    pisitools.removeDir("%s/hardcopy/XPRINT" % x11docdir)
    pisitools.remove("%s/hardcopy/Xserver/Xprt.*" % x11docdir)
    pisitools.remove("/%s/man7/Xprint.7" % get.manDIR())
