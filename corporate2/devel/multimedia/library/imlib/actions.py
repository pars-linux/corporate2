#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# GNU General Public License, 
# version 2. See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools 

def setup():
    autotools.configure("--disable-static \
                         --disable-gdk \
                         --disable-gtktest")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS","ChangeLog","README","NEWS")
