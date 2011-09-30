#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown -R havp:havp /var/log/havp")
    os.system("/bin/chown -R havp:havp /var/run/havp")
    os.system("/bin/chown -R havp:havp /var/tmp/havp")
