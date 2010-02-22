from comar.service import *
import os

serviceType = "local"
serviceDefault = "off"
serviceDesc = _({"en": "Modem Manager",
                 "tr": "Modem Yöneticisi"})

@synchronized
def start():
    startService(command="/usr/sbin/modem-manager",
                 donotify=True,
                 detach=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/modem-manager",
                donotify=True)

def status():
    return isServiceRunning(command="/usr/sbin/modem-manager")
