#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "squid-%s" % get.srcVERSION().replace("0.", "0.STABLE")

def setup():
    autotools.configure('--enable-shared=yes \
                         --enable-static=no \
                         --enable-xmalloc-statistics \
                         --enable-carp \
                         --enable-async-io \
                         --enable-storeio="aufs,diskd,ufs" \
                         --enable-removal-policies="heap,lru" \
                         --enable-icmp \
                         --enable-delay-pools \
                         --disable-esi \
                         --enable-icap-client \
                         --enable-ecap \
                         --enable-useragent-log \
                         --enable-referer-log \
                         --enable-wccp \
                         --enable-wccpv2 \
                         --disable-kill-parent-hack \
                         --enable-snmp \
                         --enable-cachemgr-hostname="localhost" \
                         --enable-arp-acl \
                         --enable-htcp \
                         --enable-ssl \
                         --enable-forw-via-db \
                         --enable-follow-x-forwarded-for \
                         --enable-cache-digests \
                         --disable-poll \
                         --enable-epoll \
                         --enable-linux-netfilter \
                         --disable-ident-lookups \
                         --enable-default-hostsfile=/etc/hosts \
                         --enable-auth="basic,digest,negotiate,ntlm" \
                         --enable-basic-auth-helpers="getpwnam,LDAP,MSNT,multi-domain-NTLM,NCSA,PAM,SMB,YP,SASL,POP3,DB,squid_radius_auth" \
                         --enable-ntlm-auth-helpers="fakeauth,no_check,smb_lm" \
                         --enable-negotiate-auth-helpers="squid_kerb_auth" \
                         --enable-digest-auth-helpers="password,ldap,eDirectory" \
                         --enable-external-acl-helpers="ip_user,ldap_group,session,unix_group,wbinfo_group" \
                         --with-pthreads \
                         --with-dl \
                         --with-large-files \
                         --with-build-environment=default \
                         --with-default-user=squid \
                         --enable-mit=/usr \
                         --enable-http-violations \
                         --enable-zph-qos \
                         --sysconfdir=/etc/squid \
                         --localstatedir=/var \
                         --libexecdir=/usr/lib/squid \
                         --datadir=/usr/share/squid \
                         --with-logdir=/var/log/squid')

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/cache/squid")
    pisitools.dodir("/var/log/squid")

    pisitools.dosym("/usr/share/squid/errors/en", "/etc/squid/errors")

    pisitools.doman("helpers/basic_auth/LDAP/*.8")
    pisitools.dohtml("helpers/basic_auth/MSNT/README.html", "RELEASENOTES.html")
    pisitools.dodoc("helpers/basic_auth/SASL/squid_sasl_auth*")
    pisitools.dodoc("CONTRIBUTORS", "CREDITS", "ChangeLog", "QUICKSTART", "doc/*.txt", "helpers/ntlm_auth/no_check/README.no_check_ntlm_auth")
