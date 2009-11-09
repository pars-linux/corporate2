#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "p7zip_%s" % get.srcVERSION()

def build():
    autotools.make('OPTFLAGS="%s -DHAVE_GCCVISIBILITYPATCH -fvisibility=hidden -fvisibility-inlines-hidden" \
                    all3' % get.CFLAGS())

def install():
    pisitools.insinto("/usr/lib/p7zip","bin/*")

    # p7zip wrapper
    pisitools.dobin("contrib/gzip-like_CLI_wrapper_for_7z/p7zip")
    pisitools.doman("contrib/gzip-like_CLI_wrapper_for_7z/man1/p7zip.1")

    pisitools.dohtml("DOCS/MANUAL/*")
    pisitools.dodoc("ChangeLog", "README", "TODO", "DOCS/*.txt")
