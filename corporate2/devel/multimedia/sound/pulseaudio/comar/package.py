#!/usr/bin/python

import os

PULSE_DIR="/var/lib/pulse"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if os.path.exists(PULSE_DIR):
        os.system("chown pulse:pulse %s" % PULSE_DIR)
        os.chmod(PULSE_DIR, 0700)

