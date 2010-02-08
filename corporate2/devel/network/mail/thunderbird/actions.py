#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "mozilla"

shelltools.export("CFLAGS", "%s -Os -fno-strict-aliasing" % get.CFLAGS())

def setup():
    shelltools.system("./configure --prefix=/usr --libdir=/usr/lib")

def build():
    autotools.make()

    #compile language files
    locales = ["be", "ca", "de", "es-AR", "es-ES", "fr", "it", "nl", "pl", "pt-BR", "sv-SE", "tr"]

    for locale in locales:
        autotools.make("-C mail/locales libs-%s" % locale)
        pisitools.copy("mozilla/dist/xpi-stage/locale-%s/chrome/%s.jar" % (locale, locale), "mozilla/dist/bin/chrome/")
        pisitools.copy("mozilla/dist/xpi-stage/locale-%s/chrome/%s.manifest" % (locale, locale), "mozilla/dist/bin/chrome/")

def install():
    pisitools.insinto("/usr/lib/", "mozilla/dist/bin", "MozillaThunderbird", sym=False)

    # Fake symlinks to get Turkish spell check support working
    pisitools.dosym("/usr/lib/MozillaThunderbird/dictionaries/en-US.aff","/usr/lib/MozillaThunderbird/dictionaries/tr-TR.aff")
    pisitools.dosym("/usr/lib/MozillaThunderbird/dictionaries/en-US.dic","/usr/lib/MozillaThunderbird/dictionaries/tr-TR.dic")

    # Install icon
    pisitools.insinto("/usr/share/pixmaps", "other-licenses/branding/thunderbird/mailicon256.png", "thunderbird.png")

    # Install docs
    pisitools.dodoc("mozilla/LEGAL", "mozilla/LICENSE")
