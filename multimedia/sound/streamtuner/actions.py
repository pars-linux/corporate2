#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domo("streamtuner.po" , "tr" , "streamtuner.mo")

    pisitools.removeDir("/usr/share/help")
    pisitools.removeDir("/usr/share/omf")

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "HACKING", "QUICKSTART", "README", "TODO")
