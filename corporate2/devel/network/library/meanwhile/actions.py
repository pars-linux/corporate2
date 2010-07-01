#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-doxygen=no \
                         --enable-static=no \
                         --disable-mailme")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("README", "ChangeLog", "AUTHORS", "COPYING", "LICENSE", "TODO")

    doc_dir = "%s/usr/share/doc/meanwhile-doc-%s" % (get.installDIR(), get.srcVERSION())
    shelltools.copytree("%s/samples" % doc_dir,
                        "%s/usr/share/doc/%s" % (get.installDIR(),
                                                 get.srcNAME()))
    shelltools.unlinkDir(doc_dir)

