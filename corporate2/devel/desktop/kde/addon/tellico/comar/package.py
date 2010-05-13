#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from comar import service

service.loadEnvironment()
kdedir = os.environ["KDEDIR"]

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/xmlcatalog --noout --add \"delegatePublic\" \
               \"-//Robby Stephenson/DTD Tellico V9.0//EN\" \
               \"file://%s/share/apps/tellico/tellico.dtd\" \
               /etc/xml/catalog" % kdedir)

    os.system("/usr/bin/xmlcatalog --noout --add \"delegateSystem\" \
               \"http://www.periapsis.org/tellico/dtd/v9/tellico.dtd\" \
               \"file://%s/share/apps/tellico/tellico.dtd\" \
               /etc/xml/catalog" % kdedir)

    os.system("/usr/bin/xmlcatalog --noout --add \"delegateURI\" \
               \"http://www.periapsis.org/tellico/dtd/v9/tellico.dtd\" \
               \"file://%s/share/apps/tellico/tellico.dtd\" \
               /etc/xml/catalog" % kdedir)

def preRemove():
    os.system("/usr/bin/xmlcatalog --noout --del \
               \"file://%s/share/apps/tellico/tellico.dtd\" \
               /etc/xml/catalog" % kdedir)
