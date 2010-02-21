#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import dbus
import gobject
from dbus.mainloop.glib import DBusGMainLoop

DBUS_INTERFACE_PROPERTIES='org.freedesktop.DBus.Properties'
MM_DBUS_SERVICE='org.freedesktop.ModemManager'
MM_DBUS_PATH='/org/freedesktop/ModemManager'
MM_DBUS_INTERFACE='org.freedesktop.ModemManager'
MM_DBUS_INTERFACE_MODEM='org.freedesktop.ModemManager.Modem'
MM_DBUS_INTERFACE_MODEM_CDMA='org.freedesktop.ModemManager.Modem.Cdma'
MM_DBUS_INTERFACE_MODEM_GSM_CARD='org.freedesktop.ModemManager.Modem.Gsm.Card'
MM_DBUS_INTERFACE_MODEM_GSM_NETWORK='org.freedesktop.ModemManager.Modem.Gsm.Network'

dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

#dev = sys.argv[1]

# Connect to DBus
bus = dbus.SystemBus()

"""
# Get proxy and d-bus interface
manager_proxy = bus.get_object(MM_DBUS_SERVICE, MM_DBUS_PATH)
manager_iface = dbus.Interface(manager_proxy, dbus_interface=MM_DBUS_INTERFACE)

for m in manager_iface.EnumerateDevices():
    modem_proxy = bus.get_object(MM_DBUS_SERVICE, m)

    # Get properties
    props_iface = dbus.Interface(modem_proxy, dbus_interface=DBUS_INTERFACE_PROPERTIES)

    if dev == props_iface.Get(MM_DBUS_INTERFACE_MODEM, 'MasterDevice'):
        print "Found device %s" % dev
        break
"""

def deviceRemoved(path):
    print "Removed device %s" % path

def deviceAdded(path):
    print "Added device %s" % path

bus.add_signal_receiver(deviceAdded, dbus_interface=MM_DBUS_SERVICE,
                        signal_name="DeviceAdded")

bus.add_signal_receiver(deviceRemoved, dbus_interface=MM_DBUS_SERVICE,
                        signal_name="DeviceRemoved")

gobject.MainLoop().run()




