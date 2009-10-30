#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")

    # Disable device node creation during build/install
    pisitools.dosed("util/Makefile.in", "mknod", "echo Disabled: mknod ")

    autotools.configure("--disable-static \
                         --disable-kernel-module \
                         --disable-rpath \
                         --exec-prefix=/ \
                         --bindir=/bin")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/etc")

    # Make compat symlinks into /usr/bin
    pisitools.dosym("/bin/fusermount", "/usr/bin/fusermount")
    pisitools.dosym("/bin/ulockmgr_server", "/usr/bin/ulockmgr_server")

    # Move pkgconfig file to /usr/lib
    pisitools.dodir("/usr/lib/pkgconfig")
    shelltools.move("%s/lib/pkgconfig/fuse.pc" % get.installDIR(), "%s/usr/lib/pkgconfig/fuse.pc" % get.installDIR())
    pisitools.removeDir("/lib/pkgconfig")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "FAQ", "Filesystems", "NEWS", "README", "README.NFS")
