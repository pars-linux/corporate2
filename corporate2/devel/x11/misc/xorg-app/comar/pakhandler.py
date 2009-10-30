# -*- coding: utf-8 -*-

import os
import piksemel
import subprocess

def updateIndex(filepath, cleanup=False):
    doc = piksemel.parse(filepath)
    indexedDirs = []
    for item in doc.tags("File"):
        path = item.getTagData("Path")
        if path.startswith("usr/share/fonts/"):
            fontDir = "/%s" % os.path.dirname(path)

            if fontDir not in indexedDirs:
                indexedDirs.append(fontDir)

                if cleanup:
                    try:
                        os.unlink(os.path.join(fontDir, "fonts.dir"))
                        os.unlink(os.path.join(fontDir, "fonts.scale"))
                    except OSError:
                        pass
                else:
                    subprocess.call(["/usr/bin/mkfontscale", "-u", fontDir])
                    subprocess.call(["/usr/bin/mkfontdir", fontDir])


def setupPackage(metapath, filepath):
    updateIndex(filepath)

def postCleanupPackage(metapath, filepath):
    updateIndex(filepath, True)
