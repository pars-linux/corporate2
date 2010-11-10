from comar.service import *
import os

serviceType = "server"
serviceDefault = "off"

serviceDesc = _({"en": "Kerberos 5 server",
                 "tr": "Kerberos 5 sunucusu"})

serviceConf = "krb5kdc"

KRB5KDC = "/usr/sbin/krb5kdc"
PIDFILE = "/var/run/krb5kdc.pid"

@synchronized
def start():
    ARGS = "-P %s" % PIDFILE

    # Check if a realm is given
    realm = config.get("KRB5REALM", "")
    if realm:
        ARGS += "-r %s" % realm

    if config.get("KRB5KDC_ARGS", ""):
        ARGS += "%s" % config.get("KRB5KDC_ARGS", "")

    startService(command=KRB5KDC,
                 args=ARGS,
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
