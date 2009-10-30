#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="gsm-1.0-pl12"

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s bindir=/usr/bin" % get.installDIR())

    for bin in ["tcat","untoast"]:
        pisitools.remove("/usr/bin/%s" % bin)
        pisitools.dosym("/usr/bin/toast", "/usr/bin/%s" % bin)

    # Move gsm.h out of gsm subdir
    pisitools.insinto("/usr/include","inc/gsm.h")
    pisitools.removeDir("/usr/include/gsm")

    # No static libs
    pisitools.remove("/usr/lib/libgsm.a")

    pisitools.dodoc("ChangeLog", "COPYRIGHT", "MACHINES", "MANIFEST", "README")
