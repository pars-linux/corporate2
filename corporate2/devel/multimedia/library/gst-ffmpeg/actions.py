#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools


def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --disable-valgrind \
                         --with-system-ffmpeg")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("README","NEWS","ChangeLog")
