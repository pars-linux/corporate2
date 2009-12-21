#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="%s" % get.srcNAME()

def install():
    pisitools.chmod("*",0644)

    pisitools.insinto("/usr/lib/perl5/vendor_perl/%s/SGMLS" % get.curPERL(), "Refs.pm")
    pisitools.insinto("/usr/lib/perl5/vendor_perl/%s/SGMLS" % get.curPERL(), "Output.pm")
    pisitools.insinto("/usr/lib/perl5/vendor_perl/%s" % get.curPERL(), "SGMLS.pm")

    pisitools.chmod("sgmlspl.pl")
    pisitools.insinto("/usr/bin","sgmlspl.pl","sgmlspl")

    pisitools.dodoc("ChangeLog","README","COPYING")
