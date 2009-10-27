#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "busybox-1.14.1"

def build():
    autotools.make("-j1")
    autotools.make("busybox.links")

def install():
    pisitools.insinto("/lib/initramfs", "busybox.links")
    pisitools.insinto("/lib/initramfs", "busybox")
