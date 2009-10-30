#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005, 2006, 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("OPT_CFLAGS='%s' EXTRA_LDFLAGS='%s'" % (get.CFLAGS(), get.LDFLAGS()))

def install():
    pisitools.insinto("/usr/lib/ladspa", "*.so")
    pisitools.insinto("/usr/share/ladspa/rdf", "*.rdf")

    pisitools.dodoc("README", "COPYING", "CREDITS")
