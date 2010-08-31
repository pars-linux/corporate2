#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure('--disable-pygtk-test \
                         --disable-oss-sound \
                         --enable-docbook-stylesheet')

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc('README', 'FAQ', 'COPYING', 'ChangeLog', 'AUTHORS')
