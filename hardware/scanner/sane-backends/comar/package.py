#!/usr/bin/python

import shutil

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    try:
        shutil.rmtree("/var/lib/lock/sane")
    except OSError:
        pass
