# -*- coding: utf-8 -*-
from comar.service import *

serviceType="server"
serviceDesc = _({"en": "MySQL Database Server",
                 "tr": "MySQL Veritabanı Sunucusu"})

MSG_ERR_MYSQLNOTINST = _({"en": "MySQL is not configured properly, please re-install the package.",
                          "tr": "MySQL düzgün yapılandırılmamış, lütfen paketi tekrar yükleyin.",
                          })

PIDFILE = "/var/run/mysqld/mysqld.pid"

def check_mysql():
    import os.path
    if not os.path.exists("/var/lib/mysql"):
        fail(MSG_ERR_MYSQLNOTINST)

@synchronized
def start():
    check_mysql()
    startService(command="/usr/sbin/mysqld",
                 pidfile=PIDFILE,
                 detach=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(PIDFILE)
