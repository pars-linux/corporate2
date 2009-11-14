#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

if "_" in get.srcVERSION():
    # Snapshot
    WorkDir = "alsa-driver"
else:
    # Upstream tarball
    WorkDir = "alsa-driver-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/include/sound/", "alsa-kernel/include/*.h")
