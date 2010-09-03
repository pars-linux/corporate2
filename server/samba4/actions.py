#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "samba-4.0.0alpha10"

def setup():
    shelltools.cd("source4/")
    autotools.configure("--enable-fhs \
                         --localstatedir=/var \
                         --libdir=/usr/lib \
                         --with-piddir=/var/run/samba \
                         --with-lockdir=/var/lib/samba \
                         --with-logfilebase=/var/log/samba \
                         --with-privatedir=/var/lib/samba/private \
                         --with-readline \
                         --disable-gnutls \
                         --enable-external-libtalloc=yes \
                         --enable-external-libtdb=yes \
                         --enable-external-libtevent=yes")

def build():
    shelltools.cd("pidl")
    perlmodules.configure()
    autotools.make()

    shelltools.cd("../source4/")
    autotools.make()

def install():
    #first install pidl and make it pidl compatible
    shelltools.cd("pidl/")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #samba joins now
    shelltools.cd("../source4/")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #do mid-level sym
    libs = ["libldb", "libndr", "libndr_standard", "libsamba-hostconfig", "libdcerpc", "libdcerpc_samr", "libsamba-util"]
    for i in libs:
        pisitools.dosym("%s.so.0.0.1" % i, "/usr/lib/%s.so.0" % i)

    # files that we dont need since openchange doesnt need'em and they conflict with smb3
    binaries = ["mount.cifs",
                "umount.cifs",
                "gentest",
                "getntacl",
                "locktest",
                "masktest",
                "ndrdump",
                "nsstest",
                "setnttoken",
                "smbtorture",
                "nmblookup",
                "smbclient",
                "cifsdd",
                "net",
                "reg*",
                "testparm",
                "wbinfo",
                "ntlm_auth",
                "ldb*"]

    sbinaries = ["samba"]

    libraries = ["libdcerpc_atsvc.*",
                 "libgensec.*",
                 "libregistry.*",
                 "libtorture.*",
                 "libnss_winbind.so*"]

    pkgconfigfiles = ["dcerpc_atsvc.pc",
                      "gensec.pc",
                      "registry.pc",
                      "torture.pc"]

    headers = ["gensec.h",
               "registry.h"]

    for bin in binaries:
        pisitools.remove("/usr/bin/%s" % bin)

    for sbin in sbinaries:
        pisitools.remove("/usr/sbin/%s" % sbin)

    for lib in libraries:
        pisitools.remove("/usr/lib/%s" % lib)

    for pkgconfig in pkgconfigfiles:
        pisitools.remove("/usr/lib/pkgconfig/%s" % pkgconfig)

    for header in headers:
        pisitools.remove("/usr/include/samba-4.0/%s" % header)

    pisitools.removeDir("/usr/lib/%s" % get.curPYTHON())
