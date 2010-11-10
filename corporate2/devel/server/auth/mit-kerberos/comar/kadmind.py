from comar.service import *
import os

serviceType = "server"
serviceDefault = "off"
serviceDesc = _({"en": "Kerberos 5 administrative server",
                 "tr": "Kerberos 5 yönetimsel sunucusu"})
serviceConf = "kadmin"

PIDFILE = "/var/run/kadmind.pid"
KADMIND = "/usr/sbin/kadmind"

MSG_ERROR_SLAVE = "Error. This appears to be a slave server, found kpropd.acl"

@synchronized
def start():
    if not os.path.exists("/var/kerberos/krb5kdc/principal"):
        # Make an educated guess -- if they're using kldap somewhere,
        # then we don't know for sure that this is an error.

    startService(command=KADMIND,
                 args=
                 donotify=True)

@synchronized
def reload():
    if os.path.exists(PIDFILE):
        # 1 is SIGHUP
        os.kill(int(open(PIDFILE, "r").read().strip()), 1)

@synchronized
def stop():
    stopService(pidfile=PIDFILE, donotify=True)

def status():
    return isServiceRunning(pidfile=PIDFILE)
