#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

import os

WorkDir = "foomatic-db-%s" % get.srcVERSION().split("_", 1)[1]
NoStrip = "/"

def setup():
    # Disable gzip compression for better lzma compression
    autotools.configure("--disable-gzip-ppds \
                         --with-drivers=NOOBSOLETES,NOEMPTYCMDLINE")

    # Cleanup conflicts
    shelltools.chmod("cleanup-conflicts.sh", 0755)
    shelltools.cd("db/source")
    shelltools.system("../../cleanup-conflicts.sh")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Fix permissions
    for root, dirs, files in os.walk("%s/usr/share/foomatic/db" % get.installDIR()):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)
