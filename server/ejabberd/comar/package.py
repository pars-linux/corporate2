#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/bash /etc/ejabberd/self-cert.sh")
    os.system("/bin/chown -R ejabberd: /var/lib/ejabberd")
    os.system("/bin/chmod -R 0750 /var/lib/ejabberd")
    os.system("/bin/chmod 0600 /var/lib/ejabberd/.erlang.cookie")
    os.system("/bin/chown -R ejabberd: /var/log/ejabberd")
    os.system("/bin/chmod -R 0750 /var/log/ejabberd")
