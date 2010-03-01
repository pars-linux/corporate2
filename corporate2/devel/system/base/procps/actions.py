#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make('CC=%s CPPFLAGS="%s" CFLAGS="%s" LDFLAGS="%s" lib64=lib' % \
                   (get.CC(), get.CXXFLAGS(), get.CFLAGS(), get.LDFLAGS()))

def install():
    autotools.rawInstall('ln_f="ln -sf" ldconfig="true" lib64=lib DESTDIR=%s' % get.installDIR())

    pisitools.insinto("/usr/include/proc/", "proc/*.h")

    # conflicts with coreutils
    pisitools.remove("/bin/kill")
    pisitools.remove("/usr/share/man/man1/kill.1")

    pisitools.dosym("libproc-%s.so" % get.srcVERSION(), "/lib/libproc.so")

    pisitools.dodoc("sysctl.conf", "BUGS", "NEWS", "TODO", "ps/HACKING")
