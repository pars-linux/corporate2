#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import scons
from pisi.actionsapi import get

WorkDir = "yafaray"

def setup():
    pisitools.dosed("config/linux2-config.py", "PREFIX = '/usr/local'", "PREFIX = '/usr'")
    pisitools.dosed("config/linux2-config.py", "CCFLAGS = '-Wall'", "CCFLAGS = '%s'" % get.CXXFLAGS())
    pisitools.dosed("config/linux2-config.py", "REL_CCFLAGS = '-O3 -ffast-math'", "REL_CCFLAGS = '-ffast-math %s'" % get.LDFLAGS())
    pisitools.dosed("config/linux2-config.py", "/share/yafaray/blender", "/share/blender/scripts")
    pisitools.dosed("config/linux2-config.py", "WITH_YF_QT='false'", "WITH_YF_QT='true'")
    pisitools.dosed("config/linux2-config.py", "YF_MISC_LIB = 'dl'\n", "YF_MISC_LIB = 'dl'\nYF_QTDIR = '/usr/qt/4'")

def install():
    scons.install("PREFIX='%s/usr' swig_install install" % get.installDIR())

    pisitools.domove("/usr/share/blender/scripts/_*.so", "/usr/lib/%s/site-packages/" % get.curPYTHON())
    pisitools.insinto("/usr/share/blender/scripts", "blender-scripts/*.py")

    pisitools.dodoc("CODING", "LICENSE")
