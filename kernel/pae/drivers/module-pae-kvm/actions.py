#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

NoStrip=["/usr/share/kvm"]
WorkDir='kvm-kmod-devel-85'

def setup():
    autotools.rawConfigure('--arch=x86 \
                            --kerneldir=/lib/modules/%s/build' % kerneltools.getKernelVersion())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())


