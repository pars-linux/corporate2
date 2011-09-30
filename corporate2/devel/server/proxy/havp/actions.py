#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get 

def setup():
    autotools.configure("--enable-clamav \
                         --enable-ssl \
                         --enable-ssl-tunnel")

def build():
    autotools.make()

def install():
    autotools.install()

    shelltools.chmod("%s/var/log/havp" % get.installDIR(), 0700)
    shelltools.chmod("%s/var/run/havp" % get.installDIR(), 0700)
    shelltools.chmod("%s/var/tmp/havp" % get.installDIR(), 0700)

    pisitools.dodoc("ChangeLog", "COPYING")
