#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde
from pisi.actionsapi import get

WorkDir = "klamav-%s-source/klamav-%s" % (get.srcVERSION(),get.srcVERSION())

shelltools.export("HOME", "%s" % get.workDIR())

def setup():
    kde.configure("--without-included-sqlite \
                   --with-disableupdates \
                   --disable-rpath")

def build():
    kde.make()

def install():
    kde.install()

    pisitools.dodoc("AUTHORS","ChangeLog","COPYING","NEWS","README")
