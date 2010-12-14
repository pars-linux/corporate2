from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "Zarafa Exchange Server",
                 "tr": "Zarafa Exchange Sunucu"})
serviceDefault = "off"

MSG_ERR_MYSQLNOTRUNNING = _({"en": "MySQL server is not running.",
                             "tr": "MySQL sunucu çalışmıyor."})

MYSQLDPID = "/var/run/mysqld/mysqld.pid"
PIDFILE = "/var/run/zarafa-server.pid"
SERVERCONFIG = "/etc/zarafa/server.cfg"

def check_mysql():
    import os.path
    if not os.path.exists(MYSQLDPID):
        fail(MSG_ERR_MYSQLNOTRUNNING)

@synchronized
def start():
    import os
    os.environ["LC_ALL"] = "C"
    os.environ["LANG"] = "C"

    check_mysql()

    startService(command="/usr/bin/zarafa-server",
                 args="-c %s" % SERVERCONFIG,
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
