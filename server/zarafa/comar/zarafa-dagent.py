from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "Zarafa LMTP Delivery Agent",
                 "tr": "Zarafa LMTP Delivery Agent"})
serviceDefault = "off"

PIDFILE = "/var/run/zarafa-dagent.pid"
DAGENTCONFIG = "/etc/zarafa/dagent.cfg"

@synchronized
def start():
    import os
    os.environ["LC_ALL"] = "C"
    os.environ["LANG"] = "C"

    startService(command="/usr/bin/zarafa-dagent",
                 args="-d -c %s" % DAGENTCONFIG,
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
