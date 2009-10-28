#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # Fixup version
    shelltools.echo(".version", get.srcVERSION().split("_")[0])

    autotools.configure()

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # binutils installs this infopage
    pisitools.remove("/usr/share/info/standards.info")

    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog*", "NEWS", "README")
