#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "glib-%s" % get.srcVERSION()

def setup():
    autotools.configure("--with-threads=posix \
                         --disable-gtk-doc \
                         --with-pcre=system \
                         --disable-fam \
                         --disable-static")

    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")
    pisitools.dosed("gthread-2.0.pc"," -pthread"," -lpthread")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/share/gtk-doc")

    pisitools.dodoc("AUTHORS", "ChangeLog*", "README*", "NEWS*")
