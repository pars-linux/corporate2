#!/usr/bin/python
# -*- coding: utf-8 -*-

import dbus
import os
import sys

def isModuleLoaded(name):
    return os.popen("grep '%s' /proc/modules" % name).read().strip() != ""

def loadModule(name):
    bus = dbus.SystemBus()
    obj = bus.get_object("tr.org.pardus.comar", "/package/module_init_tools")
    obj.load(name, "", dbus_interface="tr.org.pardus.comar.Boot.Modules")

def auth(action):
    bus = dbus.SessionBus()
    obj = bus.get_object("org.freedesktop.PolicyKit.AuthenticationAgent", "/")

    try:
        auths = obj.ObtainAuthorization("tr.org.pardus.comar.boot.modules." + action, 0, os.getpid(), dbus_interface="org.freedesktop.PolicyKit.AuthenticationAgent")
        return auths
    except Exception, e:
        print e
        return False

def main():
    if isModuleLoaded("smartcam"):
        return True
    try:
        loadModule("smartcam")
        return True
    except Exception, e:
        if e.get_dbus_name().endswith('policy.no'):
            return False
        elif e.get_dbus_name().endswith('policy.auth_admin'):
            authResult = auth("load")
        elif e.get_dbus_name().endswith('policy.auth_user'):
            authResult = auth("load")
        else:
            return False
        try:
            if authResult:
                loadModule("smartcam")
                return True
            else:
                return False
        except:
            return False

if __name__ == "__main__":
    sys.exit(not main())
