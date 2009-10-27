#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.unlink("py-compile")
    shelltools.sym("/bin/true", "py-compile")

    autotools.configure("--with-xml=libxml \
                         --localstatedir=/var \
                         --disable-doxygen-docs \
                         --disable-static \
                         --disable-xml-docs")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pythonmodules.fixCompiledPy()

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
