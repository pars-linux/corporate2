#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().replace("_", "-"))
shelltools.export("HOME", get.workDIR())

def setup():
    # This docbook is buggy
    # pisitools.dosed("doc-translations/CMakeLists.txt", "^(add_subdirectory\( pt_digikam/digikam \))$", "#\\1")

    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure(installPrefix="/usr/kde/4", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    """
    for d in ["sv"]:
        pisitools.remove("/usr/kde/4/share/doc/HTML/%s/%s/common" % (d, get.srcNAME()))
        pisitools.dosym("/usr/kde/4/share/doc/HTML/en/common", "/usr/kde/4/share/doc/HTML/%s/%s/common" % (d, get.srcNAME()))
    """
