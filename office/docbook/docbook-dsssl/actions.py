#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pass

def build():
    pass

def install():
    autotools.rawInstall("BINDIR=%s/usr/bin DESTDIR=%s/usr/share/sgml/docbook/dsssl-stylesheets-%s MANDIR=%s/%s install" % (get.installDIR(), get.installDIR(), get.srcVERSION(), get.installDIR(), get.manDIR()))

    pisitools.dosym("dsssl-stylesheets-%s" % get.srcVERSION(), "/usr/share/sgml/docbook/dsssl-stylesheets")

    #pisitools.rename("/usr/bin/collateindex.pl", "collateindex")
