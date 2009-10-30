from comar.service import *
import os

serviceType = "local"
serviceDesc = _({
    "en": "KDE Desktop Environment",
    "tr": "KDE Masaüstü Ortamı",
})
serviceDefault = "on"

def setLang():
    kdmrc_path = "/etc/X11/kdm/kdmrc"
    lang = file("/etc/mudur/language").read().rstrip("\n")

    import ConfigParser
    kdmrc = ConfigParser.ConfigParser()
    kdmrc.optionxform = str
    kdmrc.readfp(open(kdmrc_path))
    kdmrc.set('X-*-Greeter', 'Language', lang)
    kdmrc.write(open(kdmrc_path, 'wb'))

@synchronized
def start(boot=False):
    if status():
        return

    if call("zorg", "Xorg.Display", "ready", (boot,), 5 * 60) == 0:
        fail("Not starting as zorg returned an error")

    startDependencies("acpid", "hal")
    loadEnvironment()
    setLang()
    os.environ["XAUTHLOCALHOSTNAME"]=os.uname()[1]
    startService(command="/usr/kde/3.5/bin/kdm",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/kde/3.5/bin/kdm",
                donotify=True)

def status():
    return isServiceRunning("/var/run/kdm.pid")

def ready():
    if is_on() == "on":
        start(boot=True)
