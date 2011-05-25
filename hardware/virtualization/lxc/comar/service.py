from comar.service import *

serviceType = "local"
serviceDefault = "off"
serviceDesc = _({"en": "Linux Containers Management Service",
                 "tr": "Linux Kapları Yönetim Hizmeti"})
serviceConf = "lxc"

LOCKFILE="/var/lock/subsys/lxc"

import os

@synchronized
def start():
    # Start all containers listed in /etc/conf.d/lxc
    open(LOCKFILE, 'w').close()
    os.system("/usr/bin/logger -t LXC -- Service is starting...")
    for container in config.get("AUTOSTART", "").split():
        os.system("/usr/bin/logger -t LXC -- Starting container %s" % container)
        os.system("/usr/bin/screen -dmS init-%s /usr/bin/lxc-start -n %s" % (container, container))

    os.system("/usr/bin/logger -t LXC -- All containers listed in /etc/conf.d/lxc started.")

@synchronized
def stop():
    # Currently there is no way to gracefully shutdown a container.
    # Mudur is not stopping services running inside a container when
    # it recieves the TERM signal. So we must kill init of the container.
    os.system("/usr/bin/logger -t LXC -- Service is stopping...")
    for container in config.get("AUTOSTART", "").split():
        os.system("/usr/bin/logger -t LXC -- Stopping container %s" % container)
        os.system("/usr/bin/lxc-stop -n %s" % container)

    os.system("/usr/bin/logger -t LXC -- All containers listed in /etc/conf.d/lxc stopped.")
    os.remove(LOCKFILE)

def status():
    return os.path.isfile(LOCKFILE)

