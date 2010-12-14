#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "zcp-source-%s-24200" % get.srcVERSION()

shelltools.export("CFLAGS", "%s -fno-strict-aliasing" % get.CFLAGS())

def setup():
    shelltools.cd("src")
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-testtools \
                         --enable-perl \
                         --enable-debug \
                         --enable-oss \
                         --enable-release \
                         --disable-static")

def build():
    shelltools.cd("src")
    autotools.make()

def install():
    shelltools.cd("src")
    autotools.rawInstall("install-ajax-webaccess DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/etc/init.d")

    # Remove licensed stuff
    pisitools.removeDir("/etc/zarafa/report-ca")
    pisitools.removeDir("/etc/zarafa/license")

    LICENSED_STUFF = ["report", "backup", "restore", "ldapms.cfg", "licensed*"]
    for i in LICENSED_STUFF:
        pisitools.remove("%s/man?/zarafa-%s.?" % (get.manDIR(), i))

    # Move the userscripts to their correct place and symlink them
    pisitools.dodir("/usr/share/zarafa/userscripts")

    USER_SCRIPTS = ["companies_common.sh", "groups_common.sh", "users_common.sh", \
                    "createcompany", "creategroup", "createuser", "deletecompany", \
                    "deletegroup", "deleteuser"]
    for i in USER_SCRIPTS:
        pisitools.domove("/etc/zarafa/userscripts/%s" % i, "/usr/share/zarafa/userscripts")
        pisitools.dosym("/usr/share/zarafa/userscripts/%s" % i, "/etc/zarafa/userscripts/%s" % i)

    # Install some files into
    pisitools.insinto("/usr/share/zarafa", "installer/linux/db-calc-storesize")
    pisitools.insinto("/usr/share/zarafa", "installer/linux/db-convert-attachments-to-files")
    pisitools.insinto("/usr/share/zarafa", "installer/linux/ssl-certificates.sh")
    pisitools.insinto("/usr/share/zarafa", "installer/linux/db-upgrade-objectsid-to-objectguid.pl")
    pisitools.insinto("/usr/share/zarafa", "installer/linux/ldap-switch-sendas.pl")
    pisitools.insinto("/usr/share/zarafa", "installer/ldap/zarafa.schema")

    # Create default log and lib directory
    pisitools.dodir("/var/log/zarafa")
    pisitools.dodir("/var/lib/zarafa")

    # Remove unwanted/unused files that shouldn't exist anyway
    pisitools.remove("/etc/sysconfig/zarafa-indexer")
    pisitools.domove("/etc/sysconfig/zarafa", "/etc/conf.d")
    pisitools.removeDir("/etc/sysconfig")

    # Move the webaccess configuration file to its correct place
    pisitools.dodir("/etc/zarafa/webaccess")
    pisitools.domove("/etc/zarafa/webaccess-ajax/config.php", "/etc/zarafa/webaccess/")
    pisitools.removeDir("/etc/zarafa/webaccess-ajax")
    pisitools.remove("/usr/share/zarafa-webaccess/config.php")
    pisitools.dosym("/etc/zarafa/webaccess/config.php", "/usr/share/zarafa-webaccess/config.php")

    # Remove wrong webaccess plugins directory
    pisitools.removeDir("/var/lib/zarafa-webaccess/plugins")
    pisitools.remove("/usr/share/zarafa-webaccess/plugins")
    pisitools.dodir("/usr/share/zarafa-webaccess/plugins")

    # Remove unwanted webaccess files
    pisitools.remove("/usr/share/zarafa-webaccess/.htaccess")
    pisitools.remove("/usr/share/zarafa-webaccess/zarafa-webaccess.conf")
