#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/install-catalog --add /etc/sgml/openjade-%s-%s.soc \
               /usr/share/sgml/openjade-%s/catalog" % (toVersion, toRelease, toVersion))

def preRemove():
    ver = "1.3.2"
    release = "5"
    os.system("/usr/bin/install-catalog --remove /etc/sgml/openjade-%s-%s.soc \
               /usr/share/sgml/openjade-%s/catalog" % (ver, release, ver))
