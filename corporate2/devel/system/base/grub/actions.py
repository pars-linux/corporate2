#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # do not delete, testing if this line is necessary
    # shelltools.export("CFLAGS", "%s -fno-stack-protector -DNDEBUG -fno-strict-aliasing -minline-all-stringops" % get.CFLAGS())
    shelltools.export("CFLAGS", "")
    shelltools.export("LDFLAGS", "")
    shelltools.export("grub_cv_prog_objcopy_absolute", "yes")

    autotools.autoreconf()
    autotools.configure("--libdir=/lib \
                         --datadir=/usr/lib/grub \
                         --exec-prefix=/ \
                         --disable-ffs \
                         --disable-ufs2 \
                         --disable-auto-linux-mem-opt")

def build():
    autotools.make("-j1")

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.newdoc("docs/menu.lst", "grub.conf.sample")
    pisitools.dodoc("AUTHORS", "BUGS", "COPYING", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
