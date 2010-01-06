#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("CFLAGS=\"%s\"" % get.CFLAGS())
    autotools.make("convert")

def install():
    pisitools.dosed("man/Makefile", "^prefix \?= .*$", "prefix = /usr/share")
    autotools.rawInstall("bindir=/sbin DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/bin", "bcp", "btrfs-bcp")
    pisitools.insinto("/usr/bin", "show-blocks", "btrfs-show-blocks")

    pisitools.dosym("btrfsck", "/sbin/fsck.btrfs")

    pisitools.dodoc("COPYING")
