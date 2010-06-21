#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-Dlibdir=/%s/%s \
                          -Dlibexecdir=/%s \
                          -Dmoduledir=/%s/%s/%s/%s/modules" % (get.defaultprefixDIR(), "lib", get.libexecDIR(), get.defaultprefixDIR(), "lib", get.srcNAME(), get.srcVERSION()))

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "ChangeLog", "COPYING")
