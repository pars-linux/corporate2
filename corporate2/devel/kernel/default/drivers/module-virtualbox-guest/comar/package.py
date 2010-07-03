# -*- coding: utf-8 -*-

def postRemove():
    import os

    old_module_path = "/lib/modules/2.6.32.14-139/extra/vboxvfs.ko"
    if os.path.exists(old_module_path):
        os.remove(old_module_path)
