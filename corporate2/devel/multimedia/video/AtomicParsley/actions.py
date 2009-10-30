#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="atomicparsley-%s" % get.srcVERSION()

def setup():
    autotools.configure()

def build():
    autotools.make("-j1")

def install():
    pisitools.dobin("AtomicParsley")
    pisitools.dosym("AtomicParsley","/usr/bin/atomicparsley")

    pisitools.dodoc("README.txt")
