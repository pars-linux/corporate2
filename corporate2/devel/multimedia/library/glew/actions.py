#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "glew"

def build():
    autotools.make()

def install():
    autotools.rawInstall("GLEW_DEST=%s/usr" % get.installDIR())

    # Remove conflicting files with mesa package
    pisitools.remove("/usr/include/GL/glew.h")
    pisitools.remove("/usr/include/GL/glxew.h")

    pisitools.dohtml("doc/*")
    pisitools.dodoc("README.txt", "doc/*.txt")
