#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "Linux-PAM-%s" % get.srcVERSION()

def setup():
    shelltools.export("CFLAGS", "%s -fPIC -D_GNU_SOURCE" % get.CFLAGS())

    libtools.libtoolize()
    # needed by pam-0.99.10.0-unix-audit-failed.patch
    autotools.autoreconf()
    autotools.rawConfigure("--disable-prelude \
                            --enable-audit \
                            --enable-db=no \
                            --enable-nls \
                            --disable-dependency-tracking \
                            --enable-securedir=/lib/security \
                            --enable-isadir=/lib/security")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # No need for la files
    pisitools.remove("/lib/security/*.la")

    # Wrong man page
    pisitools.remove("usr/share/man/man8/pam_userdb.8*")

    pisitools.removeDir("/usr/share/doc/Linux-PAM/")
    pisitools.doman("doc/man/*.[0-9]")
    pisitools.dodoc("CHANGELOG", "Copyright", "README")
