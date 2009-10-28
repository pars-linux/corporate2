#!/usr/bin/python

import os

oldPackages = ("nvidia_drivers_old",)
currentPackage = "xorg_video_nvidia71"

def enable(package):
    call(package.replace("-", "_"), "Xorg.Driver", "enable")

def migrate():
    configXML = "/var/lib/zorg/config.xml"
    if os.path.exists(configXML):
        import piksemel

        doc = piksemel.parse(configXML)
        dirty = False
        for card in doc.tags("Card"):
            ac = card.getTag("ActiveConfig")
            if ac:
                drv = ac.getTag("Driver")
                if drv:
                    pkg = drv.getAttribute("package")
                    if pkg:
                        pkg = pkg.replace("-", "_")
                        if drv.firstChild().data() == "nvidia" \
                            and (pkg in oldPackages):
                            drv.setAttribute("package", currentPackage)
                            drv.setData("nvidia71")
                            dirty = True

        if dirty:
            open(configXML, "w").write(doc.toPrettyString())

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    try:
        os.makedirs("/etc/udev/devices")
    except OSError:
        pass

    os.system("mknod -m 0600 /etc/udev/devices/nvidia0 c 195 0")
    os.system("mknod -m 0600 /etc/udev/devices/nvidia1 c 195 1")
    os.system("mknod -m 0600 /etc/udev/devices/nvidia2 c 195 2")
    os.system("mknod -m 0600 /etc/udev/devices/nvidia3 c 195 3")
    os.system("mknod -m 0600 /etc/udev/devices/nvidiactl c 195 255")

    os.system("mknod /dev/nvidia0 c 195 0")
    os.system("mknod /dev/nvidiactl c 195 255")

    migrate()

    try:
        enabledPackage = open("/var/lib/zorg/enabled_package").read().replace("-", "_")

        if enabledPackage in oldPackages \
            or (enabledPackage == currentPackage and fromVersion != toVersion):
            enable(currentPackage)

    except IOError:
        pass
