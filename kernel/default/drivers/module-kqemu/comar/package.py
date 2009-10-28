#!/usr/bin/python

import os

def mknod(path):
    os.system("mknod '%s' c 10 62 --mode=0666" % path)

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # /dev is tmpfs, we need this for later reboots
    mknod("/lib/udev/devices/kqemu")
    # activate
    mknod("/dev/kqemu")

def preRemove():
    os.system("rm -f /lib/udev/devices/kqemu")
    os.system("rm -f /dev/kqemu")

