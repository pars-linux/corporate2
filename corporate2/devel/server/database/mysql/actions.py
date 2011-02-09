#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.unlink("%s/mysql-test/t/ssl_8k_key-master.opt" % get.curDIR())

    flags = "%s -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE \
                -fno-strict-aliasing -fwrapv \
                -fPIC" % get.CFLAGS()

    # remember this will soon be default in gcc
    if get.ARCH() == 'i686':
        flags += " -fno-omit-frame-pointer"

    # Export flags
    shelltools.export("CFLAGS", flags)
    shelltools.export("CXXFLAGS", "%s -felide-constructors -fno-rtti -fno-exceptions" % flags)

    cmaketools.configure('-DBUILD_CONFIG=mysql_release \
                          -DFEATURE_SET="community" \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DINSTALL_INCLUDEDIR=include/mysql \
                          -DINSTALL_LIBDIR=lib/mysql \
                          -DINSTALL_MANDIR=share/man \
                          -DINSTALL_MYSQLSHAREDIR=share/mysql \
                          -DINSTALL_MYSQLTESTDIR=share/mysql-test \
                          -DINSTALL_PLUGINDIR=lib/mysql/plugin \
                          -DINSTALL_SBINDIR=sbin \
                          -DINSTALL_SCRIPTDIR=bin \
                          -DINSTALL_SQLBENCHDIR=share \
                          -DINSTALL_SUPPORTFILESDIR=share/mysql \
                          -DINSTALL_DOCREADMEDIR=share/mysql \
                          -DMYSQL_DATADIR=/var/lib/mysql \
                          -DMYSQL_UNIX_ADDR=/var/run/mysqld/mysqld.sock \
                          -DENABLED_LOCAL_INFILE=ON \
                          -DENABLE_DTRACE=OFF \
                          -DWITH_EMBEDDED_SERVER=ON \
                          -DWITH_READLINE=ON \
                          -DWITH_SSL=system \
                          -DWITH_ZLIB=system', sourceDir=".")

def build():
    cmaketools.make()

    # build libmysqld.so
    shelltools.makedirs("libmysqld/work")
    shelltools.cd("libmysqld/work")

    shelltools.system("ar -x ../libmysqld.a")
    shelltools.unlink("sql_binlog.cc.o")
    shelltools.unlink("rpl_utility.cc.o")
    autotools.compile("%s -shared -Wl,-soname,libmysqld.so.0 -o libmysqld.so.0.0.1 *.o \
                          -pthread -laio -lcrypt -lssl -lcrypto -lz -lrt -lstdc++ -ldl -ldm -lc" % get.LDFLAGS())

def install():
    cmaketools.install("DESTDIR=%s" % get.installDIR())

    # Remove libmysqld.a
    pisitools.remove("/usr/lib/mysql/libmysqld.a")

    # install shared object libmysqld.so.0.0.1 and create a symlink
    pisitools.dolib("libmysqld/work/libmysqld.so.0.0.1", "/usr/lib/mysql")
    pisitools.dosym("libmysqld.so.0.0.1", "/usr/lib/mysql/libmysqld.so.0")
    pisitools.dosym("/usr/lib/mysql/libmysqld.so.0", "/usr/lib/mysql/libmysqld.so")

    ##############
    # From Fedora: libmysqlclient_r is no more. Upstream tries to replace it
    # with symlinks but that really doesn't work (wrong soname in particular).
    # We'll keep just the devel libmysqlclient_r.so link, so that rebuilding
    # without any source change is enough to get rid of dependency on
    # libmysqlclient_r.

    pisitools.remove("/usr/lib/mysql/libmysqlclient_r.so*")
    pisitools.dosym("/usr/lib/mysql/libmysqlclient.so", "/usr/lib/mysql/libmysqlclient_r.so")

    # Remove meaningless directories and static libraries
    pisitools.removeDir("/usr/data")
    pisitools.removeDir("/usr/docs")
    pisitools.remove("/usr/lib/mysql/libmysqlclient.a")
    pisitools.remove("/usr/lib/mysql/libmysqlclient_r.a")
    pisitools.remove("/usr/lib/mysql/libmysqlservices.a")

    # Extra headers
    pisitools.insinto("/usr/include/mysql", "include/my_config.h")
    pisitools.insinto("/usr/include/mysql", "include/my_dir.h")

    # Links
    pisitools.dosym("mysqlcheck", "/usr/bin/mysqlanalyze")
    pisitools.dosym("mysqlcheck", "/usr/bin/mysqlrepair")
    pisitools.dosym("mysqlcheck", "/usr/bin/mysqloptimize")


    # Config
    shelltools.chmod("scripts/mysqlaccess.conf", 0644)
    pisitools.insinto("/etc/mysql", "scripts/mysqlaccess.conf")

    # Remove x bit from ini files
    shelltools.chmod("%s/usr/share/mysql/*.ini" % (get.installDIR()), 0644)

    # Data dir
    pisitools.dodir("/var/lib/mysql")

    # Logs
    pisitools.dodir("/var/log/mysql")
    shelltools.touch("%s/var/log/mysql/mysql.log" % get.installDIR())
    shelltools.touch("%s/var/log/mysql/mysql.err" % get.installDIR())
    pisitools.dodir("/var/lib/mysql/innodb")

    # Runtime data
    pisitools.dodir("/var/run/mysqld")

    # Documents
    pisitools.dodoc("README", "COPYING")
    pisitools.dodoc("support-files/my-*.cnf")
