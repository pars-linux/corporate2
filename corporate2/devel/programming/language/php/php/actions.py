#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# package is compiled so that we support CGI, CLI and mod_php in 1 package

WorkDir = "php-%s" % get.srcVERSION()

def setup():
    # create directories for apache and fcgi's Makefiles
    shelltools.makedirs("fcgi")
    shelltools.makedirs("apache")
    # link configure script
    shelltools.sym("../configure", "fcgi/configure")
    shelltools.sym("../configure", "apache/configure")

    shelltools.export("LC_ALL", "C")
    shelltools.export("CFLAGS","%s -fwrapv" % get.CFLAGS())
    shelltools.export("NO_INTERACTION", "1")

    pisitools.dosed("configure.in", "PHP_UNAME=.*", 'PHP_UNAME="Pardus Linux 2009"')
    pisitools.dosed("ext/pgsql/config.m4", "include/postgresql", " include/postgresql/pgsql")


    # Don't touch apache.conf
    for i in pisitools.ls("sapi/*/config.m4"):
        pisitools.dosed(i, "\\-i \\-a \\-n php5", "-i -n php5")
        pisitools.dosed(i, "\\-i \\-A \\-n php5", "-i -n php5")


    autotools.autoconf()

    common_options = "--sysconfdir=/etc \
                      --cache-file=./config.cache \
                      --with-config-file-path=/etc/php \
                      --with-config-file-scan-dir=/etc/php/ext \
                      --with-zlib-dir=/usr/lib \
                      --with-libxml-dir=/usr/lib \
                      --with-jpeg-dir=/usr/lib/ \
                      --with-png-dir=/usr/lib/ \
                      --with-freetype-dir=/usr \
                      --without-pear \
                      --with-zend-vm=GOTO \
                      --with-zend-vm=SWITCH \
                      --with-pic \
                      --with-gnu-ld \
                      --with-system-tzdata=/usr/share/zoneinfo \
                      --with-mcrypt=/usr/bin/mcrypt"

    # Enable FastCGI, needs Apache disabled
    shelltools.cd("fcgi")
    autotools.configure("--enable-fastcgi \
                         --enable-force-cgi-redirect \
                         %s \
                         %s" % (common_options, extensions()))

    # Now compile with Apache enabled
    shelltools.cd("../apache")
    autotools.configure("--with-apxs2=/usr/sbin/apxs \
                         --disable-cli \
                         %s \
                         %s" % (common_options, extensions()))

def build():
    shelltools.cd("fcgi")
    autotools.make()

    shelltools.cd("../apache")
    autotools.make()

def check():
    shelltools.cd("apache")
    autotools.make("test")

def install():
    shelltools.cd("fcgi")
    autotools.rawInstall("INSTALL_ROOT=\"%s\"" % get.installDIR(), "install")
    autotools.rawInstall("INSTALL_ROOT=\"%s\"" % get.installDIR(), "install-sapi")

    shelltools.cd("../apache")
    autotools.rawInstall("INSTALL_ROOT=\"%s\"" % get.installDIR(), "install-sapi")

    shelltools.cd("..")

    pisitools.insinto("/etc/php/", "php.ini-dist", "php.ini")

    pisitools.dosed("%s/etc/php/php.ini" % get.installDIR(), "(extension_dir = .*)", ";\\1")
    pisitools.dosed("%s/etc/php/php.ini" % get.installDIR(), r";include_path = \".:/php/includes\"",
                                                             "include_path = \".:/usr/share/php5/PEAR\"")
def extensions():
    configure_disabled = []

    configure_enabled = [
        'exif', 'ftp', 'soap', 'sockets', 'sqlite-utf8', 'bcmath',
        'dom', 'wddx', 'tokenizer', 'simplexml', 'mbstring', 'calendar',
        'gd-native-ttf'
    ]
    configure_shared = [
        'dba', 'dbase', 'embedded-mysqli'
    ]
    configure_with = [
        'bz2', 'curl', 'iconv', 'mysql', 'mysqli', 'kerberos', 'sqlite', 'mime-magic',
        'xsl', 'curlwrappers', 'gdbm', 'db4', 'ldap', 'gd', 'ttf', 'gettext',
        'ncurses', 'regex=php', 'pic', 'pcre-regex', 'pgsql'
    ]
    configure_without = []

    conf = []
    for i in configure_disabled:
        conf.append("--disable-%s" % i)
    for i in configure_enabled:
        conf.append("--enable-%s " % i)
    for i in configure_shared:
        conf.append("--enable-%s=shared" % i)
    for i in configure_with:
        conf.append("--with-%s" % i)
    for i in configure_without:
        conf.append("--without-%s" % i)

    return ' '.join(conf)
