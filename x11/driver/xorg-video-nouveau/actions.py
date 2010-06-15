# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "xf86-video-nouveau-0.0.16_pre20100415"

def setup():
    autotools.autoreconf("-vif")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
