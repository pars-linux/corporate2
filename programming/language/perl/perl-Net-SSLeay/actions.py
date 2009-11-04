#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Net-SSLeay-%s" % get.srcVERSION()

def setup():
    perlmodules.configure("-- /usr/include/openssl/")

def build():
    perlmodules.make()

def install():
    perlmodules.install()

    pisitools.dodoc("Changes","README")
