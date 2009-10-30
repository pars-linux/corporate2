#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "device-mapper.%s" % get.srcVERSION()

def setup():
    autotools.configure("--sbindir=/sbin")

def build():
    autotools.make()

def install():
    autotools.install('DESTDIR=%(D)s \
                       libdir=%(D)s/lib \
                       includedir=%(D)s/usr/include' % {"D": get.installDIR()})

    libtools.gen_usr_ldscript("libdevmapper.so")
    libtools.gen_usr_ldscript("libdevmapper-event.so")

    pisitools.dodoc("COPYING*", "INTRO", "README", "VERSION", "WHATS_NEW")

