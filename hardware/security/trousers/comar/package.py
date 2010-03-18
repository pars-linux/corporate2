#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("chown tss:tss /etc/tcsd.conf")
    os.system("chown tss:tss /var/lib/tpm")
