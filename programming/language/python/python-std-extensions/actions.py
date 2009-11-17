#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "Python-%s" % get.srcVERSION()

def setup():
    shelltools.export("OPT", "%s -fPIC -fwrapv" % get.CFLAGS())
    autotools.autoconf()
    autotools.configure("--with-fpectl \
                         --enable-shared \
                         --enable-ipv6 \
                         --with-threads \
                         --with-libc='' \
                         --enable-unicode=ucs4 \
                         --with-wctype-functions")

def build():
    autotools.make()

def install():
    if shelltools.isDirectory("install"):
        shelltools.unlinkDir("install")
    autotools.rawInstall("DESTDIR=%s/install" % get.curDIR(), "altinstall")

    shelltools.cd("install")

    pisitools.dobin("usr/bin/idle")
    pisitools.insinto("/usr/lib/%s/lib-dynload" % get.curPYTHON(), "usr/lib/%s/lib-dynload/_tkinter.so" % get.curPYTHON())

    for pkg in ("idlelib", "lib-tk"):
        pisitools.insinto("/usr/lib/%s" % get.curPYTHON(), "usr/lib/%s/%s" % (get.curPYTHON(), pkg))
