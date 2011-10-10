#!/usr/bin/python
# -*- coding: utf-8 -*-

from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "LibreOffice service mode",
                 "tr": "LibreOffice servis modu"})

@synchronized
def start():
    startService(command="/opt/LibreOffice/lib/libreoffice/program/soffice.bin",
                 args="--headless accept=\"socket,host=localhost,port=8100;urp;\" -nofirststartwizard",
                 detach=True,
                 donotify=False)

@synchronized
def stop():
    stopService(command="/opt/LibreOffice/lib/libreoffice/program/soffice.bin",
                donotify=True)

def status():
    return isServiceRunning(command="/opt/LibreOffice/lib/libreoffice/program/soffice.bin")
