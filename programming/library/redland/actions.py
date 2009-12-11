#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

docdir = "/%s/%s" % (get.docDIR(), get.srcNAME())

def setup():
    autotools.autoreconf("-fi")

    #Caution!!! --enable-storages option is buggy! Do not use it, it causes storages other than memory not to be compiled!! And it's enabled by default!!
    autotools.configure("--disable-static \
                         --disable-gtk-doc \
                         --with-raptor=system \
                         --with-rasqal=system")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("*.html")
    pisitools.dodoc("AUTHORS", "ChangeLog*", "COPYING", "NEWS", "README")
