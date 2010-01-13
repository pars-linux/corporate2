#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("doc/Makefile.in", "dvips", "#dvips")

    autotools.configure("--with-x \
                         --enable-static=no")


def build():
    autotools.make("without_doc")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("Changes", "README*")

    pisitools.domove("/usr/share/t1lib/doc/*.pdf", "/usr/share/doc/t1lib")
    pisitools.removeDir("/usr/share/t1lib/doc")
