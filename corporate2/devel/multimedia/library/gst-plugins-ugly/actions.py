#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    # sidplay is in contrib.
    autotools.configure("--disable-static \
                         --disable-rpath \
                         --disable-sidplay \
                         --with-package-name=\"Pardus gstreamer-plugins-ugly package\" \
                         --with-package-origin=\"http://www.pardus.org.tr/eng\"")

def build():
    autotools.make()

def check():
    autotools.make("-C tests/check check")

def install():
    autotools.install()

    pisitools.dodoc("README", "COPYING", "AUTHORS", "NEWS")
