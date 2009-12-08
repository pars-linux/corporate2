#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools

shelltools.export('HOME', get.workDIR())
KeepSpecial=["libtool"]

def install():
    pythonmodules.install()
    binpath = "%s/bin/firewall-config" % get.kdeDIR()
    pisitools.remove(binpath)
    pisitools.dosym("%s/share/apps/firewall-config/firewall-config.py" % get.kdeDIR(), binpath)

    shelltools.chmod("%s/var/lib/iptables/pardus" % get.installDIR(), 0600)
