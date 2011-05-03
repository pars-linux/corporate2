#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="krb5-%s" % get.srcVERSION()

def setup():
    # Rebuild configure scripts
    shelltools.cd("src")
    autotools.autoheader()
    autotools.autoconf()

    # Rename man pages to regenerate them
    for manpage in open("../manpaths.txt", "r"):
        shelltools.move(manpage.strip(), "%s.in" % manpage.strip())

    shelltools.export("CFLAGS", "-I/usr/include/et -fPIC -fno-strict-aliasing -fstack-protector-all %s" % get.CFLAGS())

    # Fix pthread linking
    pisitools.dosed("configure", "-lthread", "-lpthread")
    pisitools.dosed("configure", "-pthread", "-lpthread")

    # dirsrv or ldap?
    autotools.configure("--with-system-et \
                         --with-system-ss \
                         --with-pam \
                         --with-ldap \
                         --with-netlib=-lresolv \
                         --without-selinux \
                         --without-tcl \
                         --localstatedir=/var/kerberos \
                         --disable-rpath \
                         --enable-shared \
                         --enable-pkinit \
                         --enable-dns-for-realm")

    # Fix krb5-config script to remove rpaths and CFLAGS
    pisitools.dosed("krb5-config", "^CC_LINK=.*", "CC_LINK='$(CC) $(PROG_LIBPATH)'")

def build():
    autotools.make("-C src/")

def check():
    import tempfile
    import shutil
    tmpdir = tempfile.mkdtemp(prefix='pisitest')
    autotools.make("-C src/ check TMPDIR=%s -j1" % tmpdir)
    shutil.rmtree("rm -rf %s" % tmpdir)

def install():
    shelltools.cd("src")
    autotools.rawInstall("DESTDIR=%s EXAMPLEDIR=%s/%s/%s/examples" %
            (get.installDIR(),
             get.defaultprefixDIR(),
             get.docDIR(),
             get.srcNAME()))

    # Install additional headers
    for d in ("kadm5", "krb5"):
        pisitools.insinto("/usr/include/%s" % d, "include/%s/*.h" % d)

    pisitools.dodoc("plugins/kdb/ldap/libkdb_ldap/kerberos.ldif")
    pisitools.dodoc("plugins/kdb/ldap/libkdb_ldap/kerberos.schema")

    shelltools.cd("..")

    pisitools.dodir("/var/kerberos/krb5kdc")

    for plugin in ("preauth", "kdb", "authdata"):
        pisitools.dodir("/usr/lib/krb5/plugins/%s" % plugin)

    # Install info and docs
    pisitools.doinfo("doc/*.info")
    pisitools.dodoc("README")


