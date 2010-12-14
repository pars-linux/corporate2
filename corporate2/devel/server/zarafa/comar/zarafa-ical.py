from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "Zarafa ICal Gateway",
                 "tr": "Zarafa ICal Gateway"})
serviceDefault = "off"

PIDFILE = "/var/run/zarafa-ical.pid"
ICALCONFIG = "/etc/zarafa/ical.cfg"

@synchronized
def start():
    import os
    os.environ["LC_ALL"] = "C"
    os.environ["LANG"] = "C"

    startService(command="/usr/bin/zarafa-ical",
                 args="-c %s" % ICALCONFIG,
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
