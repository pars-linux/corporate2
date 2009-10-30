#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/usr/kde/3.5/share/apps/kicker/pics/", "kside/*")
    pisitools.insinto("/usr/kde/3.5/share/apps/ksplash/Themes/Pardus/", "pardusMoodinTheme/*")
    pisitools.insinto("/usr/kde/3.5/share/wallpapers", "wallpapers/*")
    pisitools.insinto("/usr/kde/3.5/share/apps/kdm/pics/users/", "pardususer/*")
    pisitools.insinto("/usr/kde/3.5/share/apps/kicker/pics/", "kickoff/*")
    pisitools.insinto("/usr/kde/3.5/share/apps/ksmserver/pics/", "ksmserver/*")
    pisitools.insinto("/usr/kde/3.5/share/apps/kdm/pics/", "ksmserver/shutdownkonq.png", "shutdown.jpg")
    pisitools.insinto("/usr/kde/3.5/share/apps/kicker/icons/crystalsvg/32x32/apps/", "kickoff/cr32-action-leave.png", "leave.png")
    pisitools.insinto("/usr/kde/3.5/share/apps/kicker/icons/crystalsvg/48x48/apps/", "kickoff/cr32-action-leave.png", "leave.png")
    pisitools.insinto("/usr/kde/3.5/share/apps/kicker/icons/crystalsvg/32x32/apps/" ,"kickoff/cr48-app-recently_used.png", "recently_used.png")
    pisitools.insinto("/usr/kde/3.5/share/apps/kicker/icons/crystalsvg/48x48/apps/" ,"kickoff/cr48-app-recently_used.png", "recently_used.png")
