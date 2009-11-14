#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "acpica-unix-%s" % get.srcVERSION().split('_')[-1]

def build():
    autotools.make("-j1 -C tools/acpisrc")
    autotools.make("-j1 -C tools/acpixtract")
    autotools.make("-j1 -C tools/acpiexec")

    autotools.make("-j1 -C compiler/ clean")
    autotools.make("-j1 -C compiler/")

def install():
    pisitools.dobin("compiler/iasl")
    pisitools.dosbin("tools/acpisrc/acpisrc")
    pisitools.dosbin("tools/acpiexec/acpiexec")
    pisitools.dosbin("tools/acpixtract/acpixtract")

    pisitools.dodoc("changes.txt", "README")
