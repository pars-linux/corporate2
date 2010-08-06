#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("AR", "/usr/bin/ar")
    shelltools.export("RANLIB", "/usr/bin/ranlib")
    autotools.configure("--disable-multiplatform \
                         --enable-t1lib \
                         --enable-gf \
                         --with-system-t1lib \
                         --with-system-kpathsea \
                         --with-kpathsea-include=/usr/include/kpathsea")

def build():
    shelltools.cd("texk/xdvik")
    autotools.make("kpathsea_dir='/usr/include/kpathsea' texmf='/usr/share/texmf'")
    shelltools.system("/usr/bin/emacs -batch -q --no-site-file -L  -f batch-byte-compile xdvi-search.el")

def install():
    pisitools.dodir("/etc/texmf/xdvi")
    pisitools.dodir("/etc/X11/app-defaults/")

    shelltools.cd("texk/xdvik")

    autotools.install("kpathsea_dir='/usr/include/kpathsea' texmf='%s/usr/share/texmf'" % get.installDIR())

    pisitools.domove("/usr/share/texmf/xdvi/XDvi" , "/etc/X11/app-defaults/")
    pisitools.dosym("/etc/X11/app-defaults/XDvi", "/usr/share/texmf/xdvi/XDvi")

    for i in ["xdvi-ptex.sample", "xdvi.cfg"]:
        pisitools.domove("/usr/share/texmf/xdvi/%s" % i, "/etc/texmf/xdvi/")
        pisitools.dosym("/etc/texmf/xdvi/%s" % i, "/usr/share/texmf/xdvi/%s" % i)

    pisitools.insinto("/usr/share/emacs/site-lisp/tex-utils/", "*.el")

    pisitools.dodoc("BUGS", "FAQ", "README.*")
