#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

WorkDir = 'knazar'

def build():
    scons.make()

def install():
    pisitools.dobin('build/src/knazar')

    pisitools.insinto('/usr/share/applnk/Utilities/', 'src/knazar.desktop')
    pisitools.insinto('/usr/share/icons/hicolor/16x16/apps/', 'icons/hi16-app-knazar.png', 'knazar.png')
    pisitools.insinto('/usr/share/icons/hicolor/22x22/apps/', 'icons/hi22-app-knazar.png', 'knazar.png')
    pisitools.insinto('/usr/share/icons/hicolor/32x132/apps/', 'icons/hi32-app-knazar.png', 'knazar.png')

    pisitools.dodoc('COPYING', 'AUTHORS', 'ChangeLog', 'README')

    shelltools.cd("po")
    for i in shelltools.ls("*.po"):
        pisitools.domo("%s" % i, i.split('.',1)[0], "knazar.mo")
