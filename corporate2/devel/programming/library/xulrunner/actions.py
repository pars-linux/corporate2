#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

import os

WorkDir = "mozilla"
NoStrip = ["/usr/include", "/usr/share/idl"]

def setup():
    #Use autoconf-213 which we provide via a hacky pathc to produce configure
    shelltools.system("/bin/bash ./autoconf-213/autoconf-2.13 --macro-dir=autoconf-213/m4")
    shelltools.cd("js/src")

    shelltools.system("/bin/bash ../../autoconf-213/autoconf-2.13 --macro-dir=../../autoconf-213/m4")
    shelltools.cd("../..")

    autotools.configure('--enable-optimize="%s -Os -fno-strict-aliasing" --disable-strip --disable-install-strip' % get.CXXFLAGS())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    executable = ["xpcshell", "xpidl", "xpt_dump", "xpt_link",\
                  "xulrunner-stub", "mozilla-xremote-client"]

    for exe in executable:
        pisitools.dosym("/usr/lib/xulrunner-1.9/%s" % exe, "/usr/bin/%s" % exe)

    pisitools.dodir("/usr/lib/xulrunner-1.9/dictionaries")
    shelltools.touch("%s/usr/lib/xulrunner-1.9/dictionaries/tr-TR.aff" % get.installDIR())
    shelltools.touch("%s/usr/lib/xulrunner-1.9/dictionaries/tr-TR.dic" % get.installDIR())

    # Remove unnecessary executable bits
    for d in ("%s/usr/share" % get.installDIR(), "%s/usr/include" % get.installDIR()):
        for root, dirs, files in os.walk(d):
            for file in files:
                shelltools.chmod(os.path.join(root, file), 0644)
