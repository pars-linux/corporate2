#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2008-2009  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="ttf-bitstream-vera-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/fonts/bitstream-vera/", "*.ttf")
    shelltools.chmod("%s/usr/share/fonts/bitstream-vera/*" % get.installDIR(), 0644)

    pisitools.dodoc("*.TXT")
