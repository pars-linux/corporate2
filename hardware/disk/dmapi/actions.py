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
    shelltools.export("OPTIMIZER", get.CFLAGS())
    shelltools.export("DEBUG", "-DNDEBUG")

    autotools.autoconf()
    autotools.configure("--libexecdir=/usr/lib")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DIST_ROOT="%s" install-dev' % get.installDIR())

    # shared in /lib, static in /usr/lib, ldscript fun too
    pisitools.domove("/usr/lib/libdm.so*", "/lib")
    libtools.gen_usr_ldscript("libdm.so")
