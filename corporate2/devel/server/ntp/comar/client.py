#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown root:wheel /usr/bin/ntpdate")
    os.system("/bin/chmod 04710 /usr/bin/ntpdate")
