#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.export("OPTIMIZER", "%s" % get.CFLAGS())
    shelltools.export("DEBUG", "-DNDEBUG")

    autotools.configure("--bindir=/usr/bin \
                         --sbindir=/sbin \
                         --libexecdir=/usr/lib \
                         --enable-gettext")

def build():
    autotools.make("-j1 DEBUG=-DNDEBUG OPTIMIZER=\"%s\"" % get.CFLAGS())

def install():
    autotools.rawInstall("DIST_ROOT=%s" % get.installDIR())
    autotools.rawInstall("DIST_ROOT=%s" % get.installDIR(), "install-dev")

    # remove duplicated so files
    #for lib in shelltools.ls("%s/lib/lib*.so.*" % get.installDIR()):
    #    shelltools.unlink(lib)

    # shared in /lib, static in /usr/lib, ldscript fun too
    pisitools.domove("/usr/lib/lib*.so*", "/lib")

    libtools.gen_usr_ldscript("libhandle.so")
