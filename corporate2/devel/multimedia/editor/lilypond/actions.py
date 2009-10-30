#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    pisitools.dosed("config.make.in", "^elispdir = .*$", "elispdir = $(datadir)/emacs/site-lisp/lilypond")
    autotools.configure("--disable-debugging \
                         --disable-documentation \
                         --disable-gui \
                         --with-ncsb-dir=/usr/share/fonts/default/ghostscript")

def build():
    shelltools.export("LC_ALL", "C")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s vimdir=/usr/share/vim/vim72" % get.installDIR())

    pisitools.dodoc("COPYING", "NEWS.txt", "README.txt", "THANKS", "VERSION", "ROADMAP")
