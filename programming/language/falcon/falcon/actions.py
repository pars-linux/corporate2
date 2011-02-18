#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "Falcon-%s" % get.srcVERSION()

def build():
    shelltools.system("./build.sh -p %s -f %s -l %s" % (os.path.join(get.installDIR(), "usr"), "/usr/", "/lib/"))

def install():
    shelltools.system("./build.sh -i")

    pisitools.dodoc("AUTHORS", "ChangeLog", "copyright", "LICENSE*", "README", "RELNOTES", "versioninfo")
