#!/usr/bin/python

import os
import shutil

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # set the default kdm face icon if it's not already set by the system admin
    if not os.path.exists("/usr/kde/3.5/share/apps/kdm/faces/.default.face.icon"):
        os.makedirs("/usr/kde/3.5/share/apps/kdm/faces")
        shutil.copyfile("/usr/kde/3.5/share/apps/kdm/pics/users/default1.png",
                        "/usr/kde/3.5/share/apps/kdm/faces/.default.face.icon")

    if not os.path.exists("/usr/kde/3.5/share/templates/.source/emptydir"):
        os.makedirs("/usr/kde/3.5/share/templates/.source/emptydir")
