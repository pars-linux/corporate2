#!/usr/bin/python

import os

openjade = "openjade-1.3.2-3"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/install-catalog --add /etc/sgml/openjade.cat \
               /usr/share/sgml/%s/catalog" % openjade)
    os.system("/usr/bin/install-catalog --add /etc/sgml/openjade.cat \
              /usr/share/sgml/%s/dsssl/catalog" % openjade)
    os.system("/usr/bin/install-catalog --add /etc/sgml/sgml-docbook.cat \
               /etc/sgml/openjade.cat")

def preRemove():
    os.system("/usr/bin/install-catalog --remove /etc/sgml/openjade.cat \
               /usr/share/sgml/%s/catalog" % openjade)
    os.system("/usr/bin/install-catalog --remove /etc/sgml/openjade.cat \
              /usr/share/sgml/%s/dsssl/catalog" % openjade)
    os.system("/usr/bin/install-catalog --remove /etc/sgml/sgml-docbook.cat \
               /etc/sgml/openjade.cat")
