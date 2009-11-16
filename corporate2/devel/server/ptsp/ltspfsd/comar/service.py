serviceType = "server"
serviceDesc = _({"en": "Linux Terminal Server Project File System Daemon",
                 "tr": "Linux Terminal Sunucu Projesi Dosya Sistemi Servisi"})
serviceDefault = "on"

from comar.service import *

@synchronized
def start():
    startService(command="/usr/bin/ltspfsd",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/bin/ltspfsd",
                 donotify=True)

def status():
    return isServiceRunning(command="/usr/bin/ltspfsd")
