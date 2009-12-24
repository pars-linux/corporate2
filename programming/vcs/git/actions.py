#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="git-%s" % get.srcVERSION().replace("_",".")

make_git = 'CFLAGS="%s" \
            LDFLAGS="%s" \
            DESTDIR=%s \
            prefix=/usr \
            htmldir=/usr/share/doc/%s \
            INSTALLDIRS=vendor \
            GITWEB_CSS="/gitweb/gitweb.css" \
            GITWEB_LOGO="/gitweb/git-logo.png" \
            GITWEB_FAVICON="/gitweb/git-favicon.png"' % (get.CFLAGS(), get.LDFLAGS(), get.installDIR(), get.srcNAME())

def build():
    pisitools.dosed("Makefile", "^CC = .*$", "CC = %s" % get.CC())
    autotools.make('%s all doc gitweb/gitweb.cgi V=1' % make_git)

def install():
    autotools.rawInstall("%s install-doc" % make_git)

    # Emacs stuff
    pisitools.insinto("/usr/share/emacs/site-lisp", "contrib/emacs/*.el")

    # Install bash completion
    pisitools.insinto("/etc/bash_completion.d", "contrib/completion/git-completion.bash", "git")
    shelltools.chmod("%s/etc/bash_completion.d/git" % get.installDIR(), 0644)

    # gitweb
    pisitools.insinto("/var/www/localhost/cgi-bin", "gitweb/gitweb.cgi", "gitweb.cgi")
    pisitools.insinto("/var/www/localhost/cgi-bin/gitweb", "gitweb/*.css")
    pisitools.insinto("/var/www/localhost/cgi-bin/gitweb", "gitweb/*.png")

    # for git-daemon
    pisitools.dodir("/pub/scm")

    # Remove useless perl directories
    pisitools.removeDir("/usr/lib/perl5/%s" % get.curPERL())
    pisitools.removeDir("/usr/lib/perl5/vendor_perl/%s/i686-linux-thread-multi" % get.curPERL())

    # Some docs
    pisitools.dodoc("README", "COPYING", "Documentation/SubmittingPatches")
