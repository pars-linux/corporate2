#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="kqemu-%s" % get.srcVERSION().replace('_','')
NoStrip = ["/"]

KDIR = kerneltools.getKernelVersion()

cfg = {"CFLAGS": get.CFLAGS().replace("-fstack-protector", ""),
        "LDFLAGS": get.LDFLAGS(),
        "BUILDCC": get.CC(),
        "CC": "gcc",
        "KVDIR": "/lib/modules/%s/build" % KDIR,
        "KV": KDIR}

def setup():
    pisitools.dosed("configure", "`uname -r`", KDIR)
    pisitools.dosed("install.sh", "`uname -r`", KDIR)
    pisitools.dosed("common/Makefile", "-Werror")
    pisitools.dosed("common/Makefile", "pardusCFLAGS", cfg["CFLAGS"])
    pisitools.dosed("common/Makefile", "pardusCC", cfg["CC"])

    autotools.configure('--kernel-path="%(KVDIR)s" \
                         --cc="%(CC)s" \
                         --host-cc="%(BUILDCC)s" \
                         --extra-cflags="%(CFLAGS)s" \
                         --extra-ldflags="%(LDFLAGS)s"' % cfg)


def build():
    autotools.make()

def install():
    pisitools.insinto("/lib/modules/%s/extra" % KDIR, "*.ko")
