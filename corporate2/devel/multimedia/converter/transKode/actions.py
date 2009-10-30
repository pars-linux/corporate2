#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

WorkDir = 'transkode'

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()
    pisitools.dodir("/usr/kde/3.5/share/applnk/Multimedia")
    pisitools.domove("/usr/kde/3.5/share/applnk/transkode.desktop", "/usr/kde/3.5/share/applnk/Multimedia")
