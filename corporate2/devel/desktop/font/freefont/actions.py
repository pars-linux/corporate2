#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "freefont-%s" % get.srcVERSION().split("_")[1]
shelltools.export("HOME", get.workDIR())



def build():
    shelltools.system("fontforge -lang=ff -script buildscript *.sfd")

def install():
    pisitools.insinto("/usr/share/fonts/freefont/", "*.ttf")
    
    pisitools.dosym("../conf.avail/60-gnu-free-mono.conf", "/etc/fonts/conf.d/60-gnu-free-mono.conf")
    pisitools.dosym("../conf.avail/60-gnu-free-sans.conf", "/etc/fonts/conf.d/60-gnu-free-sans.conf")
    pisitools.dosym("../conf.avail/60-gnu-free-serif.conf", "/etc/fonts/conf.d/60-gnu-free-serif.conf")        
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "README",)
