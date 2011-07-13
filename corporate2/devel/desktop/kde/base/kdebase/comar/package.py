#!/usr/bin/python

import os
import shutil

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/usr/kde/3.5/share/templates/.source/emptydir"):
        os.makedirs("/usr/kde/3.5/share/templates/.source/emptydir")
