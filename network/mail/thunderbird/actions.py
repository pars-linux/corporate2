#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "thunderbird"
AUTOCONF = "autoconf-213/autoconf-2.13"
MOZAPPDIR= "/usr/lib/MozillaThunderbird"

shelltools.export("CFLAGS", "%s -Os -fno-strict-aliasing" % get.CFLAGS())
shelltools.export("CXXFLAGS", "%s -Os -fno-strict-aliasing" % get.CFLAGS())

def setup():
    shelltools.chmod(AUTOCONF, 0755)

    pisitools.dosed(".pardus-default-prefs.js", "LAUNCHER", "%s/open-browser.sh" % MOZAPPDIR)

    # FIXME: Use get.lsbINFO()
    pisitools.dosed(".pardus-default-prefs.js", "DISTRIB_ID", "Pardus")
    pisitools.dosed(".pardus-default-prefs.js", "DISTRIB_RELEASE", "Corporate2")

def build():
    autotools.make("-f client.mk build")

    # Compile language files
    locales = ["be", "ca", "de", "es-AR", "es-ES", "fr", "it", "nl", "pl", "pt-BR", "sv-SE", "tr"]

    for locale in locales:
        autotools.make("-C mail/locales libs-%s" % locale)
        pisitools.copy("mozilla/dist/xpi-stage/locale-%s/chrome/%s.jar" % (locale, locale), "mozilla/dist/bin/chrome/")
        pisitools.copy("mozilla/dist/xpi-stage/locale-%s/chrome/%s.manifest" % (locale, locale), "mozilla/dist/bin/chrome/")

def install():
    pisitools.insinto("/usr/lib/", "mozilla/dist/bin", "MozillaThunderbird", sym=False)

    # Install default-prefs.js
    pisitools.insinto("%s/greprefs" % MOZAPPDIR, ".pardus-default-prefs.js", "all-pardus.js")
    pisitools.insinto("%s/defaults/pref" % MOZAPPDIR, ".pardus-default-prefs.js", "all-pardus.js")

    # Fake symlinks to get Turkish spell check support working
    pisitools.dosym("/usr/lib/MozillaThunderbird/dictionaries/en-US.aff", "/usr/lib/MozillaThunderbird/dictionaries/tr-TR.aff")
    pisitools.dosym("/usr/lib/MozillaThunderbird/dictionaries/en-US.dic", "/usr/lib/MozillaThunderbird/dictionaries/tr-TR.dic")

    # Install icons
    pisitools.insinto("/usr/share/pixmaps", "other-licenses/branding/thunderbird/mailicon256.png", "thunderbird.png")
    pisitools.insinto("%s/icons" % MOZAPPDIR, "other-licenses/branding/thunderbird/mailicon16.png")

    for s in (16,22,24,32,48,256):
        pisitools.insinto("/usr/share/icons/hicolor/%dx%d/apps" % (s,s), "other-licenses/branding/thunderbird/mailicon%d.png" % s)

    # Install docs
    pisitools.dodoc("mozilla/LEGAL", "mozilla/LICENSE")
