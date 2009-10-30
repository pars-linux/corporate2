#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

keepSpecial=["libtool"]
shelltools.export("HOME", get.workDIR())

def setup():
    kde.make("-f admin/Makefile.common")

    # the java test is problematic (see kde bug 100729) and
    # useless. All that's needed for java applets to work is
    # to have the 'java' executable in PATH.
    shelltools.export("DO_NOT_COMPILE", "kpersonalizer")
    kde.configure("--with-dpms \
                   --enable-dnssd \
                   --with-libaudit=yes \
                   --with-hal \
                   --with-ldap \
                   --with-cups \
                   --with-gl \
                   --with-ssl \
                   --with-samba \
                   --with-libusb \
                   --with-openexr \
                   --with-libraw1394 \
                   --with-hal \
                   --with-pam=yes \
                   --with-sudo-kdesu-backend \
                   --with-krb5auth \
                   --without-arts \
                   --without-sensors \
                   --without-java")

def build():
    kde.make()

def install():
    kde.install()

    # kdm wants extra interest
    shelltools.cd("kdm")
    kde.install("GENKDMCONF_FLAGS=\"--no-old --no-backup --no-in-notice\" install")

    pisitools.remove("%s/share/templates/.source/emptydir" % get.kdeDIR())

    # Fix #730
    pisitools.remove("%s/share/autostart/ktip.desktop" % get.kdeDIR())

    # remove KDE's wallpapers, we've our own ;)
    pisitools.remove("%s/share/wallpapers/*" % get.kdeDIR())

    # remove kcontrol (we have TASMA), but not kinfocenter
    pisitools.remove("/usr/kde/3.5/bin/kinfocenter")
    pisitools.domove("/usr/kde/3.5/bin/kcontrol", "/usr/kde/3.5/bin/", "kinfocenter")
    pisitools.remove("/usr/kde/3.5/share/applications/kde/KControl.desktop")
    pisitools.remove("/usr/kde/3.5/share/applications/kde/Help.desktop")

    # Put kdmrc into /etc/X11/kdm, so it can be modified on live CDs
    pisitools.domove("/usr/kde/3.5/share/config/kdm/kdmrc", "/etc/X11/kdm/")
    pisitools.dosym("/etc/X11/kdm/kdmrc", "/usr/kde/3.5/share/config/kdm/kdmrc")

    # Remove shutdownkonq to replace it
    pisitools.remove("/usr/kde/3.5/share/apps/ksmserver/pics/shutdownkonq.png")
    pisitools.remove("/usr/kde/3.5/share/apps/kdm/pics/shutdown.jpg")

    # artwork package provides these
    pisitools.remove("/usr/kde/3.5/share/apps/kicker/pics/kside.png")
    pisitools.remove("/usr/kde/3.5/share/apps/kicker/pics/kside_tile.png")

    # Replace kicker's startup notification animation
    pisitools.remove("/usr/kde/3.5/share/apps/kicker/pics/disk*.png")
