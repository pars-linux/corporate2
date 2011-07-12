from comar.service import *

import os

serviceType = "local"
serviceDefault = "on"
serviceDesc = _({"en": "SmartCard Event Manager",
                 "tr": "Akıllı Kart Etkinlik Yöneticisi"})

PATH = "/usr/bin/pkcs11_eventmgr"
PIDFILE = "/var/run/pkcs11_eventmgr.pid"
PCSCPID = "/var/run/pcscd/pcscd.pid"

@synchronized
def start():
    if not isServiceRunning(pidfile=PCSCPID):
        startDependencies("pcsc_lite")

    startService(command="/usr/bin/pkcs11_eventmgr",
                 args="nodaemon",
                 makepid=True,
                 detach=True,
                 pidfile=PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    try:
        os.unlink(PIDFILE)
    except OSError:
        pass

def status():
    return isServiceRunning(pidfile=PIDFILE)
