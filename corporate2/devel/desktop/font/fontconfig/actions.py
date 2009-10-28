#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static \
                         --disable-docs \
                         --x-includes=/usr/include \
                         --x-libraries=/usr/lib \
                         --localstatedir=/var \
                         --with-cache-dir=/var/cache/fontconfig \
                         --with-default-fonts=/usr/share/fonts \
                         --with-add-fonts=/usr/local/share/fonts")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc/fonts", "fonts.conf", "fonts.conf.new")

    enabled_configs = ("10-sub-pixel-rgb.conf", "70-yes-bitmaps.conf")
    disabled_configs = ("10-no-sub-pixel.conf",)

    for cfg in enabled_configs:
        pisitools.dosym("../conf.avail/%s" % cfg, "/etc/fonts/conf.d/%s" % cfg)

    for cfg in disabled_configs:
        pisitools.remove("/etc/fonts/conf.d/%s" % cfg)

    for i in ["fc-cat", "fc-list", "fc-match", "fc-cache"]:
        pisitools.doman("%s/*.1" % i)

    pisitools.doman("doc/*.3")

    pisitools.dodoc("AUTHORS", "COPYING", "README", "doc/*.txt")
