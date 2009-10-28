#!/usr/bin/python

import os

oldPackages = ("nvidia_drivers",)
currentPackage = "xorg_video_nvidia96"

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
                            drv.setData("nvidia96")
                            dirty = True

        if dirty:
            open(configXML, "w").write(doc.toPrettyString())

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    migrate()

    try:
        enabledPackage = open("/var/lib/zorg/enabled_package").read().replace("-", "_")

        if enabledPackage in oldPackages \
            or (enabledPackage == currentPackage and fromVersion != toVersion):
            enable(currentPackage)

    except IOError:
        pass
