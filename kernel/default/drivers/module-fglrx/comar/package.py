#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    enabledPackage = "/var/lib/zorg/enabled_package"

    if fromVersion != toVersion \
        and os.path.exists(enabledPackage) \
        and file(enabledPackage).read().replace("-", "_") == "xorg_video_fglrx":

        call("xorg_video_fglrx", "Xorg.Driver", "enable")
