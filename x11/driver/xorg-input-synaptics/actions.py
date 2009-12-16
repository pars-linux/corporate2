# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "xf86-input-synaptics-%s" % get.srcVERSION()

def setup():
    autotools.autoreconf("-vif")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/hal/fdi/policy/10osvendor", "fdi/11-x11-synaptics.fdi")
