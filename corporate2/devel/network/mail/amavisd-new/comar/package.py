#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
        os.system("/bin/chown -R amavis:amavis /var/tmp/amavisd")
        os.system("/bin/chown -R amavis:amavis /var/db/amavisd")
        os.system("/bin/chown -R amavis:amavis /var/spool/amavis/virusmails")
        os.system("/bin/chown -R amavis:amavis /var/run/amavisd")

