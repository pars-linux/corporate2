#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    cmaketools.configure(installPrefix="/usr/kde/4")

def build():
    cmaketools.make()

def install():
    cmaketools.install("DESTDIR=%s" % get.installDIR())

