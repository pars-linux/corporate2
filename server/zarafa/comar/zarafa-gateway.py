from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "Zarafa POP3/IMAP Gateway",
                 "tr": "Zarafa POP3/IMAP Gateway"})
serviceDefault = "off"

PIDFILE = "/var/run/zarafa-gateway.pid"
GATEWAYCONFIG = "/etc/zarafa/gateway.cfg"

@synchronized
def start():
    import os
    os.environ["LC_ALL"] = "C"
    os.environ["LANG"] = "C"

    startService(command="/usr/bin/zarafa-gateway",
                 args="-c %s" % GATEWAYCONFIG,
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
