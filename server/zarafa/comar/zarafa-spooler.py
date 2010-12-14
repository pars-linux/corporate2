from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "Zarafa Spooler",
                 "tr": "Zarafa Spooler"})
serviceDefault = "off"

PIDFILE = "/var/run/zarafa-spooler.pid"
SPOOLERCONFIG = "/etc/zarafa/spooler.cfg"

@synchronized
def start():
    import os
    os.environ["LC_ALL"] = "C"
    os.environ["LANG"] = "C"

    startService(command="/usr/bin/zarafa-spooler",
                 args="-c %s" % SPOOLERCONFIG,
                 makepid=True,
                 detach=True,
                 pidfile=PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(PIDFILE)
