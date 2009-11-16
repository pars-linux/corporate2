serviceType = "server"
serviceDesc = _({"en": "Linux Terminal Server Project File System Bus Client",
                 "tr": "Linux Terminal Sunucu Projesi Dosya Sistemi Istemcisi"})
serviceDefault = "on"

from comar.service import *

@synchronized
def start():
    startService(command="/usr/bin/lbuscd",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/bin/lbuscd",
                 donotify=True)

def status():
    return isServiceRunning(command="/usr/bin/lbuscd")
