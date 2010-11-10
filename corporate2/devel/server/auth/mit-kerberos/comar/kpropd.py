from comar.service import *
import os

serviceType = "server"
serviceDefault = "off"
serviceDesc = _({"en": "Kerberos 5 propagation client",
                 "tr": "Kerberos 5 propagasyon istemcisi"})

KPROPD = "/usr/sbin/kpropd"
PIDFILE = "/var/run/cupsd.pid"
KPROPDACL = "/var/kerberos/krb5kdc/kpropd.acl"

MSG_MISSING_KPROPD = _({
                        "en" : "%s doesn't exist, exiting." % KPROPD,
                        "tr" : "%s bulunamadı." % KPROPD,
                        })

@synchronized
def start():
    if os.path.exists(KPROPDACL):
        startService(command=KPROPD,
                     args="-S",
                     donotify=True)
    else:
        # Warn
        fail(MSG_MISSING_KPROPD)

@synchronized
def stop():
    stopService(command=KPROPD,
                donotify=True)

def status():
    return isServiceRunning(command=KPROPD)
