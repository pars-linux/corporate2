#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-artsdigi \
                         --disable-esddigi \
                         --disable-jackdigi")

def build():
    autotools.make("-j1")

def install():
    autotools.install()
    autotools.make('DESTDIR="%s" install-man' % get.installDIR())

    pisitools.dodoc("AUTHORS","CHANGES","THANKS","readme.txt")
