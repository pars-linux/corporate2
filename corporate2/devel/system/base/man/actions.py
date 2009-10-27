#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="man-db-%s" % get.srcVERSION()

def setup():
     autotools.configure("--enable-dups \
                          --disable-setuid \
                          --with-device=utf8 \
                          --with-zio \
                          --with-gnu-ld \
                          --enable-mb-groff \
                          --with-db=gdbm \
                          --enable-nls \
                          --with-config-file=/etc/man.conf \
                          --disable-rpath \
                          --without-included-gettext")

def build():
    autotools.make("nls=all")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README")
