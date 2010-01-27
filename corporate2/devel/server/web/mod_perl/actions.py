#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    perlmodules.configure("MP_TRACE=0 \
                           MP_DEBUG=0 \
                           MP_USE_DSO=1 \
                           MP_APXS=/usr/sbin/apxs")

def build():
    perlmodules.make()

def check():
    # Tests fail without LC_ALL=C. This is achieved with fix-tests.patch
    # but still running test through pisi hangs. Type make test in workDIR.
    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.dodir("/var/www/localhost/cgi-perl")
