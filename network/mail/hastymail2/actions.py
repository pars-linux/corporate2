#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():

    pisitools.insinto("/etc/hastymail2", "hastymail2.conf.example", "hastymail2.conf")

    pisitools.insinto("/usr/share/hastymail2", "*")

    pisitools.dodir("/var/hastymail2")
    pisitools.dodir("/var/hastymail2/attachments")
    pisitools.dodir("/var/hastymail2/user_settings")

    pisitools.remove("/usr/share/hastymail2/INSTALL")
    pisitools.remove("/usr/share/hastymail2/hastymail2.conf.example")
    pisitools.removeDir("/usr/share/hastymail2/docs")

    pisitools.dodoc("docs/*")
    pisitools.dodoc("CHANGES", "COPYING", "README", "RELEASE_NOTES", "UPGRADING")

