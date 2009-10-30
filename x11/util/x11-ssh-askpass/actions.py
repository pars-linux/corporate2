#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()
    shelltools.system("xmkmf")

def build():
    autotools.make("includes")
    autotools.make("CDEBUGFLAGS='%s'" % get.CFLAGS())

def install():
    pisitools.insinto("/usr/lib/misc", "x11-ssh-askpass")
    pisitools.dosym("/usr/lib/misc/x11-ssh-askpass", "/usr/lib/misc/ssh-askpass")

    pisitools.dodoc("ChangeLog", "README", "TODO")
    shelltools.move("x11-ssh-askpass.man", "x11-ssh-askpass.1")
    pisitools.doman("x11-ssh-askpass.1")
