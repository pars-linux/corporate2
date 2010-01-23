#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "^PREFIX .*$", "PREFIX := /%s" % get.defaultprefixDIR())
    autotools.make("clean")

def build():
    autotools.make("CC='%s' CFLAGS='%s' LDFLAGS='%s' tuxoniceui_text tuxoniceui_fbsplash" % (get.CC(),
                                                                                             get.CFLAGS(),
                                                                                             get.LDFLAGS()))
def install():
    pisitools.dodir("/usr/sbin")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "KERNEL_API", "README", "TODO", "USERUI_API")
