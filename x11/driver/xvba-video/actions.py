# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = get.srcDIR() + ".i686"

def install():
    pisitools.insinto("/", "usr")

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")
