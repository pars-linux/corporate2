#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "kradio-snapshot_2006_09_20"

def fixmo(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)


def setup():
    kde.configure("--with-arts \
                   --enable-v4l2")

def build():
    shelltools.export("PATH", "%s:/usr/lib/%s/site-packages/unsermake" % (get.ENV("PATH"), get.curPYTHON()))
    shelltools.system("unsermake -j1")

def install():
    shelltools.system("unsermake DESTDIR=%s install" % get.installDIR())
    pisitools.remove("/usr/kde/3.5/share/applications/kde/kradio.desktop")
    pisitools.insinto("/usr/share/pixmaps", "kradio3/icons/hi64-app-kradio.png", "kradio.png")

    for d in shelltools.ls("%s/%s/share/locale/" % (get.installDIR(), get.kdeDIR())):
        pisitools.rename("%s/share/locale/%s/LC_MESSAGES/%s.mo" % (get.kdeDIR(), d, WorkDir), "kradio.mo")

