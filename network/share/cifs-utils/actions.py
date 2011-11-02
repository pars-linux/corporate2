#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    # umount.cifs is not supported anymore, so residing on umount utility of the system
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Set SUID bit for mount helper
    shelltools.chmod("%s/sbin/mount.cifs" % get.installDIR(), mode=04755)

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", )
