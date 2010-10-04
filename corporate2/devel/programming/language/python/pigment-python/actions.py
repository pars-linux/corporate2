#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2008-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fiv")
    autotools.configure("--disable-static\
                        --prefix=%s/usr" % get.installDIR())

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("COPYING", "AUTHORS", "TODO", "NEWS", "ChangeLog")
