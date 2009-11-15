#! /usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import *

# Defaults
vpi = "8"
vci = "35"
interface = "0"
encapsulation = "1" # VC-MUX

try:
    config = open("/etc/usb-modem.conf").readlines()

    for line in config:
        if line.startswith("#"):
            continue
        elif line.startswith("VPI"):
            vpi = line.split("=")[-1]
        elif line.startswith("VCI"):
            vci = line.split("=")[-1]
        elif line.startswith("Interface"):
            interface = line.split("=")[-1]
        elif line.startswith("Encapsulation"):
            encapsulation = line.split("=")[-1]
except IOError:
    pass

Popen(['/usr/sbin/br2684ctl','-c',interface,'-e',encapsulation,'-b','-a',"%s.%s" % (vpi,vci)])
