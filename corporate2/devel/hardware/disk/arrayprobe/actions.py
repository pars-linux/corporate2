#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # It's the only source directory, it's unique between all kernel flavours
    # FIXME: kerneltools has a bug which is fixed in SVN, let's handle the version here.
    autotools.configure("--kerneldir=/usr/src/linux-source-%s" % open("/etc/kernel/kernel", "r").read())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "AUTHORS", "ChangeLog", "COPYING")
