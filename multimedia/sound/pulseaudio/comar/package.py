#!/usr/bin/python
import os
import glob
import shutil

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    """
    if fromVersion == "0.9.10":
        # Upgrading from Pardus 2008
    """
    for f in glob.glob("/etc/pulse/*.newconfig"):
        shutil.move(f, f.rsplit(".newconfig")[0])

def preRemove():
    pass
