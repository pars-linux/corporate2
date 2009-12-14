#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dosbin("smartd")
    pisitools.dosbin("smartctl")

    pisitools.doman("smartd.8", "smartctl.8", "smartd.conf.5")
    pisitools.dodoc("AUTHORS","NEWS","README","WARNINGS","smartd.conf")

    pisitools.insinto("/etc/", "smartd.conf")
