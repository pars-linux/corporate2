# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import qt4

WorkDir = "doxygen-%s" % get.srcVERSION()

def setup():
    shelltools.cd("addon/doxywizard")
    qt4.configure(installPrefix="/usr/qt/4")

def build():
    qt4.make("-C addon/doxywizard")

def install():
    pisitools.dobin("bin/doxywizard")
    pisitools.doman("doc/doxywizard.1")

    pisitools.dodoc("LICENSE", "addon/doxywizard/README", "VERSION")
