#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    # Enable process accounting
    pisitools.dosed("script/bootchartd.conf", "^PROCESS_ACCOUNTING.*$", "PROCESS_ACCOUNTING=\"yes\"")
    shelltools.system("ant")

def install():
    pisitools.insinto("/usr/share/java", "bootchart.jar")

    pisitools.dodir("/sbin")
    pisitools.dodir("/etc")

    pisitools.dobin("script/bootchartd", "/sbin")
    pisitools.insinto("/etc", "script/bootchartd.conf")

    pisitools.dodoc("TODO", "COPYING", "README", "README.logger", "ChangeLog")

