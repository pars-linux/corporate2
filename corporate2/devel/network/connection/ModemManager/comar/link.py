#!/usr/bin/python
# -*- coding: utf-8 -*-

MSG_BROADBAND = {
    "en": "Broadband Networks",
    "tr": "Genişbant",
}

LABEL_REMOTE = {
    "en": "Operator",
    "tr": "Operatör",
}

LABEL_PIN_CODE = {
    "en": "Enter PIN code:",
    "tr": "PIN kodunu giriniz:",
}

AUTH_SIM_PIN = {
    "en": "SIM PIN Code",
    "tr": "SIM PIN Kodu",
}

ERROR_SIM_FAILURE = {
    "en": "No SIM card found",
    "tr": "Takılı SIM kart bulunamadı",
}

ERROR_PIN_REQUIRED = {
    "en": "PIN is required to activate the device",
    "tr": "Cihazın etkinleştirilmesi için PIN gerekli",
}

ERROR_PIN_WRONG = {
    "en": "The saved PIN code for this profile is wrong",
    "tr": "Bu profil için kaydedilmiş PIN kodu yanlış",
}

DEVICE_EDGE = {
    "en": "EDGE/GPRS",
}

DEVICE_3G = {
    "en" : "3G",
}

import os
import sys
import dbus
import time
import signal
import hashlib
import subprocess

from comar.network import listProfiles, Profile, callScript
from pardus import netutils

#######################
# Network.Link methods
#######################

DBUS_INTERFACE_PROPERTIES='org.freedesktop.DBus.Properties'
MM_DBUS_SERVICE='org.freedesktop.ModemManager'
MM_DBUS_PATH='/org/freedesktop/ModemManager'
MM_DBUS_INTERFACE='org.freedesktop.ModemManager'
MM_DBUS_INTERFACE_MODEM='org.freedesktop.ModemManager.Modem'
MM_DBUS_INTERFACE_MODEM_CDMA='org.freedesktop.ModemManager.Modem.Cdma'
MM_DBUS_INTERFACE_MODEM_GSM_CARD='org.freedesktop.ModemManager.Modem.Gsm.Card'
MM_DBUS_INTERFACE_MODEM_GSM_NETWORK='org.freedesktop.ModemManager.Modem.Gsm.Network'

NET_STACK = "baselayout"

#######################
# Internal methods    #
#######################

def _getDBusInterface():
    # Connect to D-Bus
    retval = None
    try:
        retval = dbus.SystemBus()
    except dbus.DBusException:
        pass

    return retval


def _getDeviceProxy(device):
    retval = None

    if device:
        # Create connection to D-Bus
        bus = _getDBusInterface()

        if bus:
            # Get proxy and d-bus interface
            manager_proxy = bus.get_object(MM_DBUS_SERVICE, MM_DBUS_PATH)
            manager_iface = dbus.Interface(manager_proxy, dbus_interface=MM_DBUS_INTERFACE)

            for m in manager_iface.EnumerateDevices():
                modem_proxy = bus.get_object(MM_DBUS_SERVICE, m)

                # Get properties
                props_iface = dbus.Interface(modem_proxy, dbus_interface=DBUS_INTERFACE_PROPERTIES)
                card = dbus.Interface(modem_proxy, dbus_interface=MM_DBUS_INTERFACE_MODEM_GSM_CARD)

                if device == str(card.GetImei()):
                    # Matched device
                    break

            retval = modem_proxy

    return retval

def _connect(device, number="*99#"):

    proxy = _getDeviceProxy(device)

    if not proxy:
        # FIXME: DBus error or no matching device
        return False

    if PINRequired(device):
        fail(_(ERROR_PIN_REQUIRED))
        return

    # Properties
    props_iface = dbus.Interface(proxy, DBUS_INTERFACE_PROPERTIES)
    device_node = os.path.join("/dev", str(props_iface.Get(MM_DBUS_INTERFACE_MODEM, "Device")))
    print "*** DEBUG: Got device_node %s" % device_node

    try:
        proxy.Disconnect()
        print "DEBUG: Calling Connect(\"%s\").." % number
        proxy.Connect(number)
    except dbus.DBusException, e:
        print "DEBUG: Exception: %s" % str(e)
        return (False, "")

    return (True, device_node)

def _disconnect(device):

    proxy = _getDeviceProxy(device)

    if not proxy:
        # FIXME: DBus error or no matching device
        return False

    try:
        proxy.Disconnect()
    except:
        return False

    return True

def _registerNameServers(profile, info):
    name_mode = profile.info.get("name_mode", "auto")
    name_servers = []
    name_domain = ""

    if info.has_key("IFNAME") and (info.has_key("DNS1") or info.has_key("DNS2")):
        if name_mode == "auto":
            # PPPD sometimes returns 10.11.12.13 and 10.11.12.14 as DNS servers but
            # these are buggy. Set 4.2.2.1 and 4.2.2.2 to work-around that
            name_servers = [v[1] for v in info.items() if v[0].startswith("DNS")]
            if "10.11.12.13" in name_servers and "10.11.12.14" in name_servers:
                print "DEBUG: Buggy DNS 10.11.12.*, work arounding."
                name_servers = ["4.2.2.1", "4.2.2.2"]

        call(NET_STACK, "Network.Stack", "registerNameServers", (info["IFNAME"], name_servers, name_domain))

def _unregisterNameServers(info):
    if info.has_key("IFNAME"):
        call(NET_STACK, "Network.Stack", "unregisterNameServers", (info["IFNAME"], [], ""))

def _getPPPDPids(name):
    uuid = hashlib.sha1(script()+name).hexdigest()
    pidfile = "/var/run/comar-pppd-%s.pid" % uuid
    print "DEBUG: pidfile is %s" % pidfile
    if os.path.exists(pidfile):
        return open(pidfile, "r").read().strip().split(",")

def _killPPPD(name):
    ret = _getPPPDPids(name)
    if ret:
        # Unpack
        helper_pid, pppd_pid = ret
        print "DEBUG: helper_pid: %s, pppd_pid: %s" % (helper_pid, pppd_pid)
        if helper_pid:
            print "DEBUG: Sending SIGUSR1 to %s" % helper_pid
            # Send SIGUSR1 to helper to shutdown pppd
            os.kill(int(helper_pid), signal.SIGUSR1)

def _getPPPDInfo(name):
    # Parse pppd's tdb for getting information about connection details
    print "DEBUG: name: %s" % name
    ret = _getPPPDPids(name)
    if ret:
        # Unpack
        helper_pid, pppd_pid = ret
        print "DEBUG: h_pid, pppd_pid: %s %s" % (helper_pid, pppd_pid)

        pppd_db = "/var/run/pppd2.tdb"
        if pppd_pid and os.path.exists(pppd_db):
            import tdb
            try:
                db = tdb.Tdb(pppd_db)
                info = db.get("pppd%s" % pppd_pid)
                if info:
                    db.close()
                    return dict([d.split("=") for d in info.replace("\x00", "").split(";")])
            except:
                pass


################################
# Public Network.Link Methods  #
################################

def PINRequired(device):

    proxy = _getDeviceProxy(device)

    if not proxy:
        # FIXME: DBus error or no matching device
        return False

    # GSM.Card Interface
    card = dbus.Interface(proxy, dbus_interface=MM_DBUS_INTERFACE_MODEM_GSM_CARD)

    # GSM.Network Interface
    net = dbus.Interface(proxy, dbus_interface=MM_DBUS_INTERFACE_MODEM_GSM_NETWORK)

    try:
        # Getting signal strength needs PIN. Use it for dummy checking
        net.GetSignalQuality()
    except dbus.DBusException, e:
        if "SIM PIN required" in e.get_dbus_message():
            return True

    return False

def sendPIN(device, pin):

    proxy = _getDeviceProxy(device)

    if not proxy:
        # FIXME: DBus error or no matching device
        return ""

    # GSM.Card Interface
    card = dbus.Interface(proxy, dbus_interface=MM_DBUS_INTERFACE_MODEM_GSM_CARD)

    # GSM.Network Interface
    net = dbus.Interface(proxy, dbus_interface=MM_DBUS_INTERFACE_MODEM_GSM_NETWORK)

    try:
        card.SendPin(pin)
        time.sleep(1)
    except dbus.DBusException, e:
        if "Incorrect password" in e.get_dbus_message():
            return ""
    else:
        return "True"


def deviceList():
    device_list = {}

    bus = _getDBusInterface()

    # FIXME: Using exceptions can be better
    if bus:
        # Get proxy and d-bus interface
        manager_proxy = bus.get_object(MM_DBUS_SERVICE, MM_DBUS_PATH)
        manager_iface = dbus.Interface(manager_proxy, dbus_interface=MM_DBUS_INTERFACE)

        for m in manager_iface.EnumerateDevices():
            modem_proxy = bus.get_object(MM_DBUS_SERVICE, m)

            # Get properties
            props_iface = dbus.Interface(modem_proxy, dbus_interface=DBUS_INTERFACE_PROPERTIES)

            modem_type = props_iface.Get(MM_DBUS_INTERFACE_MODEM, 'Type')
            modem_driver = props_iface.Get(MM_DBUS_INTERFACE_MODEM, 'Driver') # e.g. cdc_acm
            modem_device = props_iface.Get(MM_DBUS_INTERFACE_MODEM, 'MasterDevice') # e.g. syspath
            data_device = props_iface.Get(MM_DBUS_INTERFACE_MODEM, 'Device') # e.g. ttyACM0

            # Get properties from UDEV
            prop_dict = dict([k.split("=") for k in \
                              os.popen("udevadm info --query=property --path=%s" % modem_device).read().split()])

            # Try to enable modem
            # FIXME: This seems a little problematic, check again.
            modem_proxy.Enable(True)

            # Get IMEI for device identification
            card = dbus.Interface(modem_proxy, dbus_interface=MM_DBUS_INTERFACE_MODEM_GSM_CARD)

            # Use MM provided information for modem description if available
            modem_info = modem_proxy.GetInfo()
            if len(modem_info) > 1:
                description = str("%s %s" % (modem_info[0].capitalize(), modem_info[1]))
            else:
                # Use UDEV provided information
                description = prop_dict['ID_MODEL'].replace("_", " ")

            # Create UDEV rule for device removal detection, what a hack :)
            #_createUdevRule(prop_dict, description)

            device_list["%s:%s_%s:%s" % (prop_dict['ID_BUS'],
                                         prop_dict['ID_VENDOR_ID'],
                                         prop_dict['ID_MODEL_ID'],
                                         str(card.GetImei()))] = description



    bus.close()
    return device_list

def linkInfo():
    d = {
        "type": "broadband",
        "name": _(MSG_BROADBAND),
        "modes": "device,device_mode,auto,auth,pin,wizard",
    }
    return d

def deviceModes():
    return [
        ("edge", _(DEVICE_EDGE)),
        ("3g", _(DEVICE_3G)),
    ]

def authMethods():
    return [
            ("pin", _(AUTH_SIM_PIN)),
    ]

def authParameters(mode):
    if mode == "pin":
        return [
                ("pin", _(LABEL_PIN_CODE), "pass"),
        ]

def remoteName():
    # Sets the label in the GUI for remote AP selection
    return _(LABEL_REMOTE)

def scanRemote(device):
    from comar.network import AccessPoint

    proxy = _getDeviceProxy(device)

    if not proxy:
        # FIXME: DBus error or no matching device
        return False

    # GSM.Card Interface
    card = dbus.Interface(proxy, dbus_interface=MM_DBUS_INTERFACE_MODEM_GSM_CARD)

    # GSM.Network Interface
    net = dbus.Interface(proxy, dbus_interface=MM_DBUS_INTERFACE_MODEM_GSM_NETWORK)

    points = []
    info = {}

    # Scan
    results = net.Scan(timeout=360)
    info['ap'] = []
    info['signalstrength'] = int(net.GetSignalQuality())

    for r in results:
        status = int(r['status'])

        # Status
        # 1 -> Available
        # 2 -> Current
        # 3 -> Forbidden
        # other -> Unknown

        if status > 0 and status < 4:
            # Add to the AP list
            info['ap'].append("%s,%s,%d" % (str(r['operator-long']), str(r['operator-short']), status))

    if info:
        for ap in info['ap']:
            point = AccessPoint()
            point.ssid = ap
            point.qual = info['signalstrength']
            points.append(point.id())


    # Nothing
    return points

def getAuthMethod(name):
    profile = Profile(name)
    return profile.info.get("auth", "")

def getAuthParameters(name):
    profile = Profile(name)
    d = {}
    for key in profile.info:
        if key.startswith("auth_"):
            d[key[5:]] = profile.info[key]
    return d

def setAddress(name, mode, address, mask, gateway):
    profile = Profile(name)
    profile.info["net_mode"] = mode
    profile.info["net_address"] = address
    profile.info["net_mask"] = mask
    profile.info["net_gateway"] = gateway
    profile.save()

def setNameService(name, namemode, nameserver):
    profile = Profile(name)
    profile.info["name_mode"] = namemode
    profile.info["name_server"] = nameserver
    profile.save()

def setDeviceMode(name, mode):
    profile = Profile(name)
    profile.info["device_mode"] = mode
    profile.save()

def setRemote(name, remote):
    profile = Profile(name)
    profile.info["remote"] = remote
    profile.save()

def setAuthMethod(name, method):
    profile = Profile(name)
    profile.info["auth"] = method
    profile.save()

def setAuthParameters(name, key, value):
    profile = Profile(name)
    profile.info["auth_%s" % key] = value
    profile.save()

def setDevice(name, device):
    profile = Profile(name)
    profile.info["device"] = device
    profile.save()

def setState(name, state):
    def saveState(_state, _msg=""):
        # Save state to profile database
        if _msg:
            profile.info["state"] = _state + " " + _msg
        else:
            profile.info["state"] = _state
        profile.save(no_notify=True)
        # Notify clients
        notify("Network.Link", "stateChanged", (name, _state, _msg))
        # Run profile script
        if _state in ["down", "inaccessible", "unplugged"]:
            callScript(name, "down")
        elif _state in ["up"]:
            callScript(name, "up")


    profile = Profile(name)

    # Get needed fields from profile db
    device = profile.info["device"].split(":")[-1]
    pin = getAuthParameters(name).get("pin", "")

    print "**** setState: name:%s device:%s pin:%s state:%s" % (name, device, pin, state)
    info = {}

    # Send PIN if required and if found in profile db
    if pin and PINRequired(device):
        print "DEBUG: setState: Sending PIN"
        if not sendPIN(device, pin):
            print "DEBUG: setState: sendPIN returned false, failing."
            fail(_(ERROR_PIN_WRONG))
            return

    if state == "up":
        # Stop other profiles on same device
        # stopSameDevice(name)
        # Save state
        saveState("connecting")

        # Call connect on MM
        print "DEBUG: Calling _connect()"
        (ret, device_node) = _connect(device)
        print "DEBUG: _connect() returned: (%s, %s)" % (ret, device_node)

        if ret:
            print "DEBUG: No exception from MM, spawning comar-pppd"
            pppd_pid = subprocess.Popen(["/usr/sbin/comar-pppd",
                                         script(),
                                         name,
                                         device_node]).pid

            # Wait (max 20 seconds) for things to settle down
            # because it sometimes really takes a lot of time to connect
            for t in range(20):
                info = _getPPPDInfo(name)
                print "*** loop: info: %s" % info
                if info and info.has_key("IPREMOTE"):
                    pppd_connected = True
                    break
                print "DEBUG: Sleeping for another second for waiting pppd.."
                time.sleep(1)

            if pppd_connected:
                route = netutils.Route()
                route.setDefault(info['IPREMOTE'])

                # Register name servers
                _registerNameServers(profile, info)

                # Finally we're up
                saveState("up", info['IPLOCAL'])
            else:
                saveState("down")

        else:
            saveState("down")

    # Interface down logic
    elif state == "down":

        # Disconnect
        _disconnect(device)

        # Reset Network Stack
        _unregisterNameServers(info)

        # Shutdown PPPD
        _killPPPD(name)

        # Save state
        saveState("down")


def getState(name):
    profile = Profile(name)
    return profile.info.get("state", "down")

def deleteConnection(name):
    profile = Profile(name)
    profile.delete()
    notify("Network.Link", "connectionChanged", ("deleted", name))

def connectionInfo(name):
    profile = Profile(name)
    device = profile.info.get("device", "")
    return {
        "name": name,
        "device_id": device,
        #FIXME
        "device_name": "ozan",
        "net_address": profile.info.get("net_address", ""),
        "net_gateway": profile.info.get("net_gateway", ""),
        "name_mode": profile.info.get("name_mode", "auto"),
        "name_server": profile.info.get("name_server", ""),
        "state": profile.info.get("state", "down"),
        #"device_mode": profile.info.get("device_mode", "managed"),
        #"net_mode": profile.info.get("net_mode", "auto"),
        #"net_mask": profile.info.get("net_mask", ""),
    }

def kernelEvent(data):
    action, devpath = data.split("@", 1)
    new = True

    device_id = device = devpath

    # We don't have udev rule for add for now
    if action == "add":
        # Notify clients
        notify("Network.Link", "deviceChanged", ("add", "broadband", device_id, devpath))
        """
        # Bring related connection up
        for pn in listProfiles():
            profile = Profile(pn)
            if profile.info.get("device", None) == device_id:
                new = False
                if profile.info.get("state", "down").startswith("unplugged"):
                    setState(pn, "up")
                    break
        # Notify clients if device has no connections
        if new:
            notify("Network.Link", "deviceChanged", ("new", "broadband", device_id, netutils.deviceName(device_id)))
        """
    elif action == "remove":
        """
        # Bring related connection down
        for pn in listProfiles():
            profile = Profile(pn)
            if profile.info.get("device", "").split(":")[-1].split("_")[-1] == device:
                if profile.info.get("state", "down").startswith("up"):
                    setState(pn, "unplugged")
                    break
        # Notify clients
        """
        notify("Network.Link", "deviceChanged", ("removed", "broadband", device, ""))


def connections():
    return listProfiles()
