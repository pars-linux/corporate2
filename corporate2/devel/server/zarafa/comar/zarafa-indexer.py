from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "Zarafa Indexing Service",
                 "tr": "Zarafa Indexing Service"})
serviceDefault = "off"

PIDFILE = "/var/run/zarafa-indexer.pid"
INDEXERCONFIG = "/etc/zarafa/indexer.cfg"

@synchronized
def start():
    import os
    os.environ["LC_ALL"] = "C"
    os.environ["LANG"] = "C"

    startService(command="/usr/bin/zarafa-indexer",
                 args="-c %s" % INDEXERCONFIG,
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
