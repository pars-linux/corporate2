#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "squashfs-tools-%s-with-lzma465" % get.srcVERSION()

def build():
    autotools.make('CC="%s"' % get.CC())

def install():
    pisitools.dobin("mksquashfs")
    pisitools.dobin("unsquashfs")

    #pisitools.dodoc("CHANGES", "README-4.0", "COPYING", "ACKNOWLEDGEMENTS", "PERFORMANCE*")
