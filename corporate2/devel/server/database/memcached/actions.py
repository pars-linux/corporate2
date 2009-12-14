#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-threads")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodir("/var/run/memcached")
    shelltools.chown("%s/var/run/memcached" % get.installDIR(), "memcached", "memcached")
    shelltools.chmod("%s/var/run/memcached" % get.installDIR())

    pisitools.dodoc("AUTHORS", "README", "doc/*.txt")
