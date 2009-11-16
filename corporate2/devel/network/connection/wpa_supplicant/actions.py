#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "wpa_supplicant-%s/wpa_supplicant" % get.srcVERSION()

def setup():
    CONFIGFILE = ".config"

    shelltools.echo(CONFIGFILE, "CC = %s" % get.CC())

    # Linux specific drivers
    shelltools.echo(CONFIGFILE, "CONFIG_DRIVER_HOSTAP=y")
    shelltools.echo(CONFIGFILE, "CONFIG_DRIVER_WEXT=y")
    shelltools.echo(CONFIGFILE, "CONFIG_DRIVER_IPW=y")
    shelltools.echo(CONFIGFILE, "CONFIG_DRIVER_ATMEL=y")
    shelltools.echo(CONFIGFILE, "CONFIG_DRIVER_NDISWRAPPER=y")
    shelltools.echo(CONFIGFILE, "CONFIG_DRIVER_PRISM54=y")
    shelltools.echo(CONFIGFILE, "CONFIG_DRIVER_WIRED=y")

    # Basic authentication methods
    shelltools.echo(CONFIGFILE, "CONFIG_TLS=openssl")
    shelltools.echo(CONFIGFILE, "CONFIG_IEEE8021X_EAPOL=y")
    shelltools.echo(CONFIGFILE, "CONFIG_EAP_MD5=y")
    shelltools.echo(CONFIGFILE, "CONFIG_EAP_GTC=y")
    shelltools.echo(CONFIGFILE, "CONFIG_EAP_OTP=y")
    shelltools.echo(CONFIGFILE, "CONFIG_EAP_PSK=y")
    shelltools.echo(CONFIGFILE, "CONFIG_EAP_PAX=y")
    shelltools.echo(CONFIGFILE, "CONFIG_EAP_TLV=y")
    shelltools.echo(CONFIGFILE, "CONFIG_EAP_PEERKEY=y")
    shelltools.echo(CONFIGFILE, "CONFIG_PKCS12=y")
    shelltools.echo(CONFIGFILE, "CONFIG_EAP_LEAP=y")
    shelltools.echo(CONFIGFILE, "CONFIG_EAP_MSCHAPV2=y")
    shelltools.echo(CONFIGFILE, "CONFIG_EAP_PEAP=y")
    shelltools.echo(CONFIGFILE, "CONFIG_EAP_TLS=y")
    shelltools.echo(CONFIGFILE, "CONFIG_EAP_TTLS=y")

    # Smart card authentication
    shelltools.echo(CONFIGFILE, "CONFIG_SMARTCARD=y")
    #shelltools.echo(CONFIGFILE, "CONFIG_EAP_SIM=y")
    #shelltools.echo(CONFIGFILE, "CONFIG_EAP_AKA=y")
    #shelltools.echo(CONFIGFILE, "CONFIG_PCSC=y")

    # Basic configuration
    shelltools.echo(CONFIGFILE, "CONFIG_READLINE=y")
    shelltools.echo(CONFIGFILE, "CONFIG_CTRL_IFACE=y")
    shelltools.echo(CONFIGFILE, "CONFIG_CTRL_IFACE_DBUS=y")

def build():
    autotools.make()
    autotools.make("eapol_test")

def install():
    for bin in ["wpa_cli","wpa_passphrase", "eapol_test"]:
        pisitools.dobin(bin)

    pisitools.dosbin("wpa_supplicant")

    pisitools.insinto("/etc/dbus-1/system.d", "dbus-wpa_supplicant.conf", "wpa_supplicant.conf")

    pisitools.doman("doc/docbook/*.5")
    pisitools.doman("doc/docbook/*.8")
    pisitools.newdoc("wpa_supplicant.conf", "wpa_supplicant.conf.example")
    pisitools.dodoc("ChangeLog", "../COPYING", "eap_testing.txt", "../README", "todo.txt", "examples/*")

