#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("./regen.sh")
    autotools.configure("--enable-largefile-server \
                         --enable-supergroups \
                         --with-krb5-conf=/usr/bin/krb5-config \
                         --disable-kernel-module \
                         --disable-strip-binaries AFS_SYSKVERS=26 XCFLAGS='%s -D_LARGEFILE64_SOURCE' SHLIB_LDFLAGS='%s'" % (get.CFLAGS(), get.LDFLAGS()))

def build():
    autotools.make("-j1 all_nolibafs LDFLAGS='%s'" % get.LDFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s install_nolibafs" % get.installDIR())

    # Remove static libraries
    pisitools.remove("/usr/lib/*.a")
    pisitools.remove("/usr/lib/afs/*.a")

    pisitools.domove("/usr/lib/pam_afs.so.1", "/lib/security", "pam_afs.so")
    pisitools.domove("/usr/lib/pam_afs.krb.so.1", "/lib/security", "pam_afs.krb.so")
    shelltools.chmod("%s/lib/security/*.so" % get.installDIR(), 0755)

    pisitools.domove("/usr/bin/kpasswd", "/usr/bin", "kpasswd_afs")
    pisitools.domove("/usr/share/man/man1/kpasswd.1", "/usr/share/man/man1", "kpasswd_afs.1")

    pisitools.doman("src/pam/pam_afs.5")

    for d in ("/etc/openafs", "/var/cache/openafs", "/var/lib/openafs/db", "/var/lib/openafs/logs"):
        pisitools.dodir(d)

    # Adjust permissions
    shelltools.chmod("%s/var/lib/openafs" % get.installDIR(), 0700)
    shelltools.chmod("%s/var/lib/openafs/db" % get.installDIR(), 0700)
    shelltools.chmod("%s/var/lib/openafs/logs" % get.installDIR(), 0755)

    # Link logfiles to /var/log
    pisitools.dosym("/var/lib/openafs/logs", "/var/log/openafs")

    pisitools.removeDir("/usr/lib/openafs")

    pisitools.dodoc("README", "NEWS")

