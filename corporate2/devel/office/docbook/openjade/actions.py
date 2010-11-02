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

def setup():
    autotools.configure("--disable-static \
                         --enable-splibdir=/usr/lib \
                         --datadir=/usr/share/sgml/%s-%s" % (get.srcNAME(), get.srcVERSION()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("install install-man DESTDIR=%s" % get.installDIR())

    pisitools.dosym("openjade", "/usr/bin/jade")
    shelltools.echo("%s/%s/man1/jade.1" % (get.installDIR(), get.manDIR()), ".so man1/openjade.1")

    # add unversioned/versioned catalog and symlink
    # FIXME: This will cause corrupted files on pisi check
    pisitools.dodir("/etc/sgml")
    shelltools.touch("%s/etc/sgml/%s.soc" % (get.installDIR(), get.srcTAG()))
    pisitools.dosym("%s.soc" % get.srcTAG(), "/etc/sgml/%s.soc" % get.srcNAME())

    for i in ["dsssl/dsssl.dtd", "dsssl/style-sheet.dtd", "dsssl/fot.dtd", "dsssl/catalog"]:
        pisitools.insinto("/usr/share/sgml/%s-%s" % (get.srcNAME(), get.srcVERSION()), i)

    pisitools.dodoc("COPYING", "NEWS", "README", "VERSION")
