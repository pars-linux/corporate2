#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make('OPT="%s" \
                    CC="%s" \
                    SHARED="yes" \
                    IDSDIR="/usr/share/misc" \
                    MANDIR="/usr/share/man" \
                    all' % (get.CFLAGS(), get.CC()))

def install():
    autotools.rawInstall('DESTDIR="%s" \
                          SHARED="yes" \
                          IDSDIR="/usr/share/misc" \
                          MANDIR="/usr/share/man" \
                          install-lib' % get.installDIR())

