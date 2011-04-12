#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

arch = "i386" if get.ARCH() == "i686" else "x86_64"

WorkDir = "%s-%s-2092.%s.linux" % (get.srcNAME(), get.srcVERSION(), arch)

def build():
    # Flashplugin hack for Opera, see pardus #13989
    autotools.compile("-shared -fPIC -L/opt/netscape/plugins/ -lflashplayer \
                       -o libflashplayer.so -Wl,-rpath \
                       /opt/netscape/plugins/ opera-flash-workaround.c")

def install():
    shelltools.system("./install --prefix /usr --repackage %s/usr" % get.installDIR())

    pisitools.insinto("/usr/lib/opera/plugins/", "libflashplayer.so")

    # Remove kde4 plugin since we don't use KDE4 in Corporate2
    pisitools.remove("/usr/lib/opera/liboperakde4.so")
