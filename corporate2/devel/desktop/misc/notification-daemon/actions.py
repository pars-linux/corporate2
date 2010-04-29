#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-schemas-install \
                         --disable-static")

    shelltools.cd("notification-daemon-engine-nodoka-0.1.0")
    autotools.configure()

def build():
    autotools.make()
    autotools.make("-C notification-daemon-engine-nodoka-0.1.0")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("-C notification-daemon-engine-nodoka-0.1.0 DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
