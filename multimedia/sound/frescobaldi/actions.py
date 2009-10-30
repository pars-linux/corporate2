#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

shelltools.export("HOME", get.workDIR())

def setup():
    cmaketools.configure(installPrefix="/usr/kde/4", sourceDir=".")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "README", "THANKS")

    pythonmodules.fixCompiledPy("/usr/kde/4/share/apps/frescobaldi/lib/frescobaldi_app") 
    pythonmodules.fixCompiledPy("/usr/kde/4/share/apps/frescobaldi/lib")
