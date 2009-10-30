#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "alleggl"

def setup():
    pisitools.dosed("configure", "-Wl", "%s -Wl" % get.LDFLAGS())
    pisitools.dosed("make/makefile.unx", "ldconfig", "/bin/true")

    autotools.autoreconf("-fi")
    autotools.configure()

def build():
    autotools.make('CFLAGS="%s -ffast-math" lib' % get.CFLAGS())

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodoc("changelog", "bugs.txt", "faq.txt", "gpl.txt", "readme.txt", "quickstart.txt")
