serviceType = "server"
serviceDesc = _({"en": "OpenLDAP Server",
                 "tr": "OpenLDAP Sunucusu"})
serviceConf = "slapd.conf"

from comar.service import *

def start():
    import os
    os.environ["LC_ALL"] = "C"
    os.environ["LANG"] = "C"

    args = ["-u", "ldap", "-g", "ldap", "-h"]
    args.extend(config.get("SERVE", "ldap://").split())
    args.extend(config.get("OPTS", "").split())

    startService(command="/usr/libexec/slapd",
                 args=args,
                 pidfile="/var/run/openldap/slapd.pid",
                 donotify=True)

def stop():
    stopService(pidfile="/var/run/openldap/slapd.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/openldap/slapd.pid")
