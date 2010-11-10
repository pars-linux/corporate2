from comar.service import *
import os

serviceType = "server"
serviceDefault = "off"
serviceDesc = _({"en": "Kerberos 5 administrative server",
                 "tr": "Kerberos 5 yönetimsel sunucusu"})
serviceConf = "kadmin"

PIDFILE = "/var/run/kadmind.pid"
KADMIND = "/usr/sbin/kadmind"

MSG_ERROR_DB = _({
                        "en" : "Error. Default principal database does not exist.",
                        "tr" : "Hata. Öntanımlı temel veritabanı bulunamadı",
                 })

MSG_ERROR_SLAVE = _({
                        "en" : "Error. This appears to be a slave server, found kpropd.acl",
                        "tr" : "Hata. kpropd.acl dosyası bulundu, bu bir köle sunucu olabilir.",
                    })


@synchronized
def start():
    if not os.path.exists("/var/kerberos/krb5kdc/principal"):
        # Make an educated guess -- if they're using kldap somewhere,
        # then we don't know for sure that this is an error.
        fail(MSG_ERROR_DB)

    if os.path.exists("/var/kerberos/krb5kdc/kpropd.acl"):
        fail(MSG_ERROR_SLAVE)

    ARGS = "-P %s" % PIDFILE

    # Check if a realm is given
    realm = config.get("KRB5REALM", "")
    if realm:
        ARGS += "-r %s" % realm

    if config.get("KADMIND_ARGS", ""):
        ARGS += "%s" % config.get("KADMIND_ARGS", "")

    startService(command=KADMIND,
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
