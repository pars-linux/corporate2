#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    # don't remove --with-debugger as it is needed for reverse dependencies
    autotools.configure("--with-python \
                         --with-crypto \
                         --with-debugger \
                         --disable-static")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for i in ["", "-python"]:
        pisitools.rename("/%s/libxslt%s-%s" % (get.docDIR(), i, get.srcVERSION()), "libxslt%s" % i)

    pisitools.dodoc("AUTHORS", "ChangeLog", "Copyright", "FEATURES", "NEWS", "README", "TODO")
