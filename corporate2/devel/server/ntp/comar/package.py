#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown ntp:ntp /var/lib/ntp -R")
