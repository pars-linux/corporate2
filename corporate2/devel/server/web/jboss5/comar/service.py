#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from comar.service import *

serviceDefault = "off"
serviceType = "server"
serviceDesc = _({"en": "JBoss Application Server",
                 "tr": "JBoss Uygulama Sunucusu"
                 })

BASEDIR = "/opt/jboss5"
PIDFILE = "/var/run/jboss5.pid"

os.environ["LC_ALL"] = "C"
os.environ["LANG"] = "C"
os.environ["JAVA_HOME"] = "/opt/sun-jdk"
os.environ["JBOSS_HOME"] = BASEDIR

@synchronized
def start():
    startService(command="%s/bin/run.sh" % BASEDIR,
                 detach=True,
                 donotify=True)

@synchronized
def stop():
    stopService(command = "%s/bin/shutdown.sh" % BASEDIR,
                args="--shutdown",
                donotify = True)

def status():
    return isServiceRunning(PIDFILE)
