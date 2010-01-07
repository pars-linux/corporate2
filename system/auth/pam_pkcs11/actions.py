#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():

    autotools.configure("--disable-dependency-tracking \
                         --without-docbook")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Move pam module to /lib
    pisitools.domove("/usr/lib/security/pam_pkcs11.so", "/lib")

    # Remove *.a files and empty security directory.
    # We can't use --disable-static because of the broken build system
    shelltools.system("rm -rf %s/usr/lib/%s/*.{a,la}" % (get.installDIR(), get.srcNAME()))
    pisitools.removeDir("/usr/lib/security")

    # Create necessary directories
    pisitools.dodir("/etc/pam_pkcs11/cacerts")
    pisitools.dodir("/etc/pam_pkcs11/crls")

    # Install conf files
    for f in shelltools.ls("%s/usr/share/%s/*conf*" % (get.installDIR(), get.srcNAME())):
        pisitools.insinto("/etc/pam_pkcs11", f, shelltools.baseName(f).rstrip(".example"))

    pisitools.doman("doc/*.[18]")

    pisitools.dodoc("NEWS", "README", "doc/README*")
    pisitools.dohtml("doc/api/*.html")
