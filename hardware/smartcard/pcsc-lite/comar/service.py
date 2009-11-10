from comar.service import *

serviceType = "local"
serviceDefault = "off"
serviceDesc = _({"en": "PC/SC SmartCard Reader Service",
                 "tr": "PC/SC Akıllı Kart Okuyucu Servisi"})

@synchronized
def start():
    startDependencies("hal")

    # pcscd wont start if these exist
    import os
    if os.path.exists("/var/run/pcscd.comm"):
        os.unlink("/var/run/pcscd.comm")
    if os.path.exists("/var/run/pcscd.pub"):
        os.unlink("/var/run/pcscd.pub")

    startService(command="/usr/sbin/pcscd",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/pcscd",
                donotify=True)

def status():
    return isServiceRunning(command="/usr/sbin/pcscd")
