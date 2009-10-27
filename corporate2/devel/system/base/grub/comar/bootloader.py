import os
import os.path
import shutil

from pardus.diskutils import EDD
from pardus.fileutils import FileLock
from pardus.grubutils import grubEntry, grubCommand, grubConf

# l10n

FAIL_TIMEOUT = _({
    "en": "Request timed out.",
    "tr": "Talep zaman aşımına uğradı.",
    "fr": "Durée de requête écoulée.",
    "es": "Tiempo de espera superada.",
    "de": "Wartezeit ist abgelaufen.",
    "nl": "Wachttijd is afgelopen.",
})

FAIL_NOGRUB = {
    "en": "Grub is not properly installed.",
    "tr": "Grub düzgün bir şekilde kurulu değil.",
    "fr": "Grub n'est pas installé correctement.",
    "es": "Grub no está instalado correctamente.",
    "de": "Grub ist nicht ordningsgemäss installiert.",
    "nl": "Grub is niet op de juiste wijze geïnstalleerd.",
}

FAIL_NOENTRY = _({
    "en": "No such entry.",
    "tr": "Böyle bir kayıt bulunmuyor.",
    "fr": "Il n'existe aucune entrée de ce nom-là.",
    "es": "Entrada no exise.",
    "de": "Dieser Eintrag existiert nicht.",
    "nl": "Deze invoer bestaat niet.",
})

FAIL_NOPARDUSENTRY = _({
    "en": "There should be at least one Pardus kernel entry.",
    "tr": "En az bir Pardus çekirdek girsisi tanımlı olmalı.",
    "fr": "Il devrait y avoir au moins une entrée pour Pardus",
    "es": "Debería haber al menos una entrada con un kernel de Pardus.",
    "de": "Es sollte mindestens einen Eintrag mit einem Pardus-Kernel geben.",
    "nl": "Er dient tenminste een kernel-invoer voor Pardus te zijn.",
})

FAIL_NODEVICE = _({
    "en": "No such device: '%s'",
    "tr": "Böyle bir aygıt yok: '%s'",
    "fr": "Matériel introuvable: '%s'",
    "es": "No hay dispositivo: '%s'",
    "de": "Gerät nicht vorhanden : '%s'",
    "nl": "Onbekend apparaat: '%s'",
})

FAIL_NOSYSTEM = _({
    "en": "No such system.",
    "tr": "Böyle bir sistem türü bulunmuyor.",
    "fr": "Système introuvable.",
    "es": "Sistema no existe.",
    "de": "System nicht vorhanden.",
    "nl": "Onbekend systeem.",
})

FAIL_NOTITLE = _({
    "en": "Title must be given.",
    "tr": "Başlık belirtilmeli.",
    "fr": "Vous devez donner un titre.",
    "es": "Favor ingresar un título.",
    "de": "Bitte einen Titel eingeben.",
    "nl": "Titel dient ingevoerd te worden.",
})

FAIL_NOROOT = _({
    "en": "Root drive must be given.",
    "tr": "Kök sürücü belirtilmeli.",
    "fr": "Vous devez indiquer une partition racine.",
    "es": "Partición raíz debe ser indicada.",
    "de": "Root-Partition muss angegeben werden.",
    "nl": "Root-partitie dient opgegeven te worden.",
})

FAIL_NOKERNEL = _({
    "en": "Kernel path must be given.",
    "tr": "Çekirdek yolu belirtilmeli.",
    "fr": "Vous devez indiquer le chemin vers le noyau.",
    "es": "Ruta al kernel debe ser ingresado.",
    "de": "Bitte Pfad zum Kernel eingeben.",
    "nl": "Pad naar kernel dient opgegeven te worden.",
})

FAIL_KERNEL_IN_USE = _({
    "en": "Kernel is in use or not installed: '%s'",
    "tr": "Çekirdek kullanımda ya da yüklü değil: '%s'",
    "fr": "Soit le noyau est en cours d'utilisation, soit il n'est pas installé: %s",
    "es": "Kernel está en uso o no se encuentra: '%s'",
    "de": "Kernel ist gerade in Benutzung oder kann nicht gefunden werden: '%s'",
    "nl": "Kernel is in gebruik of niet geïnstalleerd: '%s'",
})

FAIL_KERNEL_VERSION = _({
    "en": "Kernel version must be in version-release(-suffix) format.",
    "tr": "Kernel sürümü sürüm-yayım(-uzantı) formatında olmalı.",
    "fr": "La version du noyau doit être mentionnée dans le format version-release(-suffixe)",
    "es": "Versión de kernel debe tener el formato version-release(-suffix).",
    "de": "Kernelversion muss im Format version-release(-suffix) sein.",
    "nl": "Kernelversie dient in versie-uitgave(-suffix) formaat te zijn.",
})

# Grub parser configuration

BOOT_DIR = "/boot"
GRUB_DIR = "/boot/grub"
MODULES_DIR = "/lib/modules"

TIMEOUT = 3.0
MAX_ENTRIES = 3

# Supported operating systems and required fields

SYSTEMS = {
    "linux": ("Linux", ["root", "kernel"], ["initrd", "options"]),
    "xen": ("Xen", ["root", "kernel"], ["initrd", "options"]),
    "windows": ("Windows", ["root"], []),
    "memtest": ("Memtest", ["root"], []),
}

# Grub parser

class grubParser:
    def __init__(self, _dir, write=False, timeout=-1):
        self.dir = _dir
        self.write = write
        self.grub_conf = os.path.join(_dir, "grub.conf")

        self.lock = FileLock("%s/.grub.lock" % _dir)
        try:
            self.lock.lock(write, timeout)
        except IOError:
            fail(FAIL_TIMEOUT)

        # Fail if grub is not installed
        if os.path.exists(self.grub_conf):
            self.config = grubConf()
            self.config.parseConf(self.grub_conf)
        else:
            self.fail(FAIL_NOGRUB)

    def fail(self, msg):
        self.lock.unlock()
        fail(_(msg))

    def release(self, save=True):
        if save and self.write:
            self.config.write(self.grub_conf)
        self.lock.unlock()


class ParseError(Exception):
    pass

def parseVersion(version):
    """Parses a kernel filename and returns kernel version and suffix. Raises ParseError"""
    import re
    try:
        k_version, x, x, k_suffix = re.findall("kernel-(([a-z0-9\._]+)-([0-9]+))(-.*)?", version)[0]
    except IndexError:
        raise ParseError
    return k_version, k_suffix

def getDeviceMap():
    import subprocess
    subprocess.call(["/sbin/modprobe", "edd"])

    edd = EDD()
    mbr_list = edd.list_mbr_signatures()
    edd_list = edd.list_edd_signatures()

    edd_keys = edd_list.keys()
    edd_keys.sort()

    devices = []

    i = 0
    for bios_num in edd_keys:
        edd_sig = edd_list[bios_num]
        if edd_sig in mbr_list:
            devices.append(("hd%s" % i, mbr_list[edd_sig],))
            i += 1

    return devices

def parseLinuxDevice(device):
    for grub_disk, linux_disk in getDeviceMap():
        if device.startswith(linux_disk):
            part = device.replace(linux_disk, "", 1)
            if part:
                if part.startswith("p"):
                    grub_part = int(part[1:]) - 1
                else:
                    grub_part = int(part) - 1
                return linux_disk, part, grub_disk, grub_part
    return False

def parseGrubDevice(device):
    try:
        disk, part = device.split(",")
    except ValueError:
        return False
    disk = disk[1:]
    part = part[:-1]
    if not part.isdigit():
        return False
    for grub_disk, linux_disk in getDeviceMap():
        if disk == grub_disk:
            linux_part = int(part) + 1
            if linux_disk[-1].isdigit():
                linux_part = "p%s" % linux_part
            return grub_disk, part, linux_disk, linux_part
    return False

def grubAddress(device):
    try:
        linux_disk, linux_part, grub_disk, grub_part = parseLinuxDevice(device)
    except (ValueError, TypeError):
        fail(FAIL_NODEVICE % device)
    return "(%s,%s)" % (grub_disk, grub_part)

def linuxAddress(device):
    try:
        grub_disk, grub_part, linux_disk, linux_part = parseGrubDevice(device)
    except (ValueError, TypeError):
        fail(FAIL_NODEVICE % device)
    return "%s%s" % (linux_disk, linux_part)

def getKernelData(command):
    kernel_version = None
    kernel_root = None
    if command.key == "kernel":
        kernel = command.value
        if kernel.startswith("("):
            kernel = kernel.split(")", 1)[1]
        if " " in kernel:
            kernel, parameters = kernel.split(" ", 1)
        else:
            parameters = ""
        parameters = parameters.split()
        for param in parameters:
            if param.startswith("root="):
                kernel_root = param.split("root=", 1)[1]
                kernel_version = kernel.split("kernel-")[-1]
                break
    return kernel_version, kernel_root

def bootParameters(root):
    s = []
    for i in [x for x in open("/proc/cmdline", "r").read().split() if not x.startswith("init=") and not x.startswith("xorg=")]:
        if i.startswith("root="):
            s.append("root=%s" % root)
        elif i.startswith("mudur="):
            mudur = "mudur="
            for p in i[len("mudur="):].split(','):
                if p == "livecd" or p == "livedisk": continue
                mudur += p
            if not len(mudur) == len("mudur="):
                s.append(mudur)
        else:
            s.append(i)
    return " ".join(s).strip()

def getRoot():
    for mount in os.popen("/bin/mount").readlines():
        mount_items = mount.split()
        if mount_items[2] == "/":
            if mount_items[0].startswith("/dev"):
                return mount_items[0]
            elif mount_items[0].startswith("LABEL="):
                return getDeviceByLabel(mount_items[0].split('=',1)[1])

def getDeviceByLabel(_f):
    f = os.path.join("/dev/disk/by-label/%s" % _f)
    if os.path.islink(f):
        return "/dev/%s" % os.readlink(f)[6:]
    else:
        return None

def getDeviceByUUID(_f):
    f = os.path.join("/dev/disk/by-uuid/%s" % _f)
    if os.path.islink(f):
        return "/dev/%s" % os.readlink(f)[6:]
    else:
        return None

def getUUIDByDevice(_f):
    for f in os.listdir("/dev/disk/by-uuid"):
        if _f == ("/dev/%s" % os.readlink("/dev/disk/by-uuid/%s" % f)[6:]):
            return f

    return None

def md5crypt(password):
    import random
    import md5
    des_salt = list('./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    salt, magic = str(random.random())[-8:], '$1$'

    ctx = md5.new(password)
    ctx.update(magic)
    ctx.update(salt)

    ctx1 = md5.new(password)
    ctx1.update(salt)
    ctx1.update(password)

    final = ctx1.digest()

    for i in range(len(password), 0 , -16):
        if i > 16:
            ctx.update(final)
        else:
            ctx.update(final[:i])

    i = len(password)

    while i:
        if i & 1:
            ctx.update('\0')
        else:
            ctx.update(password[:1])
        i = i >> 1
    final = ctx.digest()

    for i in range(1000):
        ctx1 = md5.new()
        if i & 1:
            ctx1.update(password)
        else:
            ctx1.update(final)
        if i % 3: ctx1.update(salt)
        if i % 7: ctx1.update(password)
        if i & 1:
            ctx1.update(final)
        else:
            ctx1.update(password)
        final = ctx1.digest()

    def _to64(v, n):
        r = ''
        while (n-1 >= 0):
            r = r + des_salt[v & 0x3F]
            v = v >> 6
            n = n - 1
        return r

    rv = magic + salt + '$'
    final = map(ord, final)
    l = (final[0] << 16) + (final[6] << 8) + final[12]
    rv = rv + _to64(l, 4)
    l = (final[1] << 16) + (final[7] << 8) + final[13]
    rv = rv + _to64(l, 4)
    l = (final[2] << 16) + (final[8] << 8) + final[14]
    rv = rv + _to64(l, 4)
    l = (final[3] << 16) + (final[9] << 8) + final[15]
    rv = rv + _to64(l, 4)
    l = (final[4] << 16) + (final[10] << 8) + final[5]
    rv = rv + _to64(l, 4)
    l = final[11]
    rv = rv + _to64(l, 2)

    return rv

def parseGrubEntry(entry):
    os_entry = {
        "os_type": "linux",
        "title": entry.title,
    }
    for command in entry.commands:
        key = command.key
        value = command.value

        if key in ["root", "rootnoverify"]:
            os_entry["root"] = linuxAddress(value)

        elif key == "uuid":
            os_entry["uuid"] = value

        elif key == "initrd":
            os_entry["initrd"] = value
            if os_entry["initrd"].startswith("("):
                os_entry["initrd"] = os_entry["initrd"].split(")", 1)[1]

        elif key == "kernel":
            try:
                kernel, options = value.split(" ", 1)
                os_entry["kernel"] = kernel
                os_entry["options"] = options

                if "root=" in options:
                    # This is a linux kernel
                    os_entry["os_type"] = "linux"

            except ValueError:
                os_entry["kernel"] = value
            if os_entry["kernel"].startswith("("):
                root, kernel = os_entry["kernel"].split(")", 1)
                os_entry["root"] = linuxAddress(root + ")")
                os_entry["kernel"] = kernel
            if os_entry["kernel"] == "/boot/xen.gz":
                os_entry["os_type"] = "xen"
            elif os_entry["kernel"] == "/boot/memtest":
                os_entry["os_type"] = "memtest"
                del os_entry["kernel"]

        elif key in ["chainloader", "makeactive"]:
            os_entry["os_type"] = "windows"

        elif key == "savedefault":
            os_entry["default"] = "saved"

        elif key == "module" and os_entry["os_type"] == "xen":
            if value.startswith("("):
                value = value.split(")", 1)[1]
            if value.startswith("/boot/kernel"):
                if " " in value:
                    os_entry["kernel"], os_entry["options"] = value.split(" ", 1)
                else:
                    os_entry["kernel"] = value
            elif value.startswith("/boot/init"):
                os_entry["initrd"] = value
    return os_entry

def makeGrubEntry(title, os_type, root=None, kernel=None, initrd=None, options=None):
    if os_type not in SYSTEMS:
        fail(FAIL_NOSYSTEM)

    fields_req = SYSTEMS[os_type][1]
    fields_opt = SYSTEMS[os_type][2]
    fields_all = fields_req + fields_opt

    if "root" in fields_all:
        if "root" in fields_req and not root:
            fail(FAIL_NOROOT)

        uuid = None
        if not root.startswith("/dev/"):
            uuid = root
            root = getDeviceByUUID(root)
            if not root:
                fail(FAIL_NODEVICE % uuid)

        try:
            linux_disk, linux_part, grub_disk, grub_part = parseLinuxDevice(root)
        except (ValueError, TypeError):
            fail(FAIL_NODEVICE % root)
        grub_device = "(%s,%s)" % (grub_disk, grub_part)

    if "kernel" in fields_req and not kernel:
        fail(FAIL_NOKERNEL)

    entry = grubEntry(title)

    if os_type == "windows":
        # If Windows is not on first disk...
        if grub_disk != "hd0":
            entry.setCommand("map", "(%s) (hd0)" % grub_disk)
            entry.setCommand("map", "(hd0) (%s)" % grub_disk, append=True)
        entry.setCommand("rootnoverify", grub_device)
        entry.setCommand("makeactive", "")
        entry.setCommand("chainloader", "+1")
    else:
        if uuid:
            entry.setCommand("uuid", uuid)
        elif root:
            entry.setCommand("root", grub_device)
    if os_type == "xen":
        entry.setCommand("kernel", "/boot/xen.gz")
        if kernel and "kernel" in fields_all:
            if options and "options" in fields_all:
                entry.setCommand("module", "%s %s" % (kernel, options))
            else:
                entry.setCommand("module", kernel)
        if initrd and "initrd" in fields_all:
            entry.setCommand("module", initrd, append=True)
    elif os_type == "memtest":
        entry.setCommand("root", grub_device)
        entry.setCommand("kernel", "/boot/memtest")
    else: # linux
        if kernel and "kernel" in fields_all:
            if options and "options" in fields_all:
                entry.setCommand("kernel", "%s %s" % (kernel, options))
            else:
                entry.setCommand("kernel", kernel)
        if initrd and "initrd" in fields_all:
            entry.setCommand("initrd", initrd)
    return entry

def removeKernel(version):
    dir_modules = os.path.join(MODULES_DIR, version)
    if os.path.exists(dir_modules):
        shutil.rmtree(dir_modules)

    files_kernel = ["kernel", "System.map", "Module.sysmvers", "initramfs", "initrd", "vmlinux"]
    for _file in files_kernel:
        _file = os.path.join(BOOT_DIR, "%s-%s" % (_file, version))
        if os.path.exists(_file):
            os.unlink(_file)

# Boot.Loader methods

def listSystems():
    return SYSTEMS

def getOptions():
    grub = grubParser(GRUB_DIR, write=False, timeout=TIMEOUT)
    options = {
        "default": grub.config.getOption("default", "0"),
        "timeout": grub.config.getOption("timeout", "0"),
    }
    if "password" in grub.config.options:
        options["password"] = "yes"
    if "background" in grub.config.options:
        options["background"] = grub.config.getOption("background")
    if "splashimage" in grub.config.options:
        splash = grub.config.getOption("splashimage")
        if ")" in splash:
            splash = splash.split(")")[1]
        options["splash"] = splash
    grub.release()
    return options

def setOption(option, value):
    grub = grubParser(GRUB_DIR, write=True, timeout=TIMEOUT)
    if option == 'default':
        grub.config.setOption("default", value)
        for index, entry in enumerate(grub.config.entries):
            if value == "saved":
                entry.setCommand("savedefault", "")
            else:
                entry.unsetCommand("savedefault")
    elif option in 'timeout':
        grub.config.setOption("timeout", value)
    elif option == 'password':
        grub.config.setOption("password", "--md5 %s" % md5crypt(value))
    elif option == 'background':
        grub.config.setOption("background", value)
    elif option == 'splash':
        root = getRoot()
        root_grub = grubAddress(root)
        grub.config.setOption("splashimage", "%s%s" % (root_grub, value))
    grub.release()
    notify("Boot.Loader", "Changed", "option")

def listEntries():
    grub = grubParser(GRUB_DIR, write=False, timeout=TIMEOUT)
    entries = []
    for index, entry in enumerate(grub.config.entries):
        os_entry = parseGrubEntry(entry)
        os_entry["index"] = str(index)
        if not entry.getCommand("savedefault"):
            default_index = grub.config.getOption("default", "0")
            if default_index != "saved" and int(default_index) == index:
                os_entry["default"] = "yes"
        entries.append(os_entry)
    grub.release()
    return entries

def updateKernelEntry(version, root):
    grub = grubParser(GRUB_DIR, write=True, timeout=TIMEOUT)

    if version.startswith("kernel-"):
        version = version.split("kernel-")[1]

    if root == "":
        # Reads root partition from /bin/mount's output
        root = getRoot()

    try:
        new_version, new_suffix = parseVersion("kernel-%s" % version)
    except ParseError:
        fail(FAIL_KERNEL_VERSION)

    # Find Pardus kernels
    entries = []
    versions = {}
    for entry in grub.config.entries:
        try:
            os_entry = parseGrubEntry(entry)
        except:
            continue

        # 'root' can be undefined if the user has decided to use 'uuid'
        # instead of it.

        if "root" in os_entry:
            # Using root
            rootIsValid = (os_entry["root"] == root)
        elif "uuid" in os_entry:
            rootIsValid = (getDeviceByUUID(os_entry["uuid"]) == root)
        else:
            # No root or uuid found in entry. This is bad.
            fail(FAIL_NO_ROOT)

        if rootIsValid and os_entry["os_type"] in ["linux", "xen"]:
            try:
                kernel = os_entry["kernel"].split("/")[-1]
                kernel_version = kernel.split("kernel-")[1]
                k_version, k_suffix = parseVersion(kernel)
            except (IndexError, ParseError):
                # Not a Pardus kernel, continue
                continue
            if k_suffix == new_suffix:
                entries.append(entry)
                versions[k_version] = entry

    # Find default entry
    default = grub.config.options.get("default", 0)
    if default == "saved":
        default_index = grub.config.getSavedIndex()
    else:
        default_index = int(default)
    if default_index >= len(grub.config.entries):
        default_index = 0
    default_entry = None
    if len(grub.config.entries):
        default_entry = grub.config.entries[default_index]

    if new_version not in versions:
        # Build new entry
        release = open("/etc/pardus-release", "r").readline().strip()
        title = "%s [%s]" % (release, version)

        os_type = "linux"
        if new_suffix == "-dom0":
            os_type = "xen"

        if not len(entries):
            index = -1
            boot_parameters = bootParameters(root)
        else:
            index = grub.config.indexOf(entries[0])
            boot_parameters = parseGrubEntry(entries[0])["options"]

        kernel = "/boot/kernel-%s%s" % (new_version, new_suffix)
        initrd = "/boot/initramfs-%s%s" % (new_version, new_suffix)
        new_entry = makeGrubEntry(title, os_type, root, kernel, initrd, boot_parameters)

        if grub.config.getOption("default", "0") == "saved":
            new_entry.setCommand("savedefault", "")

        grub.config.addEntry(new_entry, index)

        # Remove old kernels
        if MAX_ENTRIES > 0:
            for x in entries[MAX_ENTRIES - 1:]:
                grub.config.removeEntry(x)
    else:
        new_entry = versions[new_version]

    # Update default index if required
    if default_entry in entries:
        updated_index = grub.config.indexOf(new_entry)
    elif default_entry in grub.config.entries:
        updated_index = grub.config.indexOf(default_entry)
    else:
        updated_index = 0
    if default != "saved":
        grub.config.setOption("default", updated_index)

    grub.release()
    notify("Boot.Loader", "Changed", "entry")

def removeEntry(index, title, uninstall):
    grub = grubParser(GRUB_DIR, write=True, timeout=TIMEOUT)
    index = int(index)
    if 0 <= index < len(grub.config.entries):
        entry = grub.config.entries[index]
        if entry.title != title:
            fail(FAIL_NOENTRY)
        default_entry = None
        default = grub.config.options.get("default", 0)
        if default != "saved":
            default = int(default)
            if default >= len(grub.config.entries):
                default = 0
            if len(grub.config.entries):
                default_entry = grub.config.entries[default]
        if uninstall == "yes":
            os_entry = parseGrubEntry(entry)
            if os_entry["os_type"] in ["linux", "xen"] and os_entry["root"] == getRoot():
                kernel_version = os_entry["kernel"].split("kernel-")[1]
                removeKernel(kernel_version)
        grub.config.removeEntry(entry)
        if default_entry in grub.config.entries:
            grub.config.setOption("default", grub.config.indexOf(default_entry))
        else:
            grub.config.setOption("default", "0")
        grub.release()
        notify("Boot.Loader", "Changed", "entry")
    else:
        fail(FAIL_NOENTRY)

def listUnused():
    grub = grubParser(GRUB_DIR, write=False, timeout=TIMEOUT)

    root = getRoot()

    # Find kernel entries
    kernels_in_use = []
    for entry in grub.config.entries:
        os_entry = parseGrubEntry(entry)

        # os_entry can have root or uuid depending on the distribution
        if os_entry["os_type"] in ["linux", "xen"]:
            if os_entry.get("root", "") == root or getDeviceByUUID(os_entry.get("uuid", "")) == root:
                kernel_version = os_entry["kernel"].split("kernel-")[1]
                kernels_in_use.append(kernel_version)

    # Find installed kernels
    kernels_installed = []
    for _file in os.listdir(BOOT_DIR):
        if _file.startswith("kernel-"):
            kernel_version = _file.split("kernel-")[1]
            kernels_installed.append(kernel_version)

    kernels_unused = set(kernels_installed) - set(kernels_in_use)
    kernels_unused = list(kernels_unused)

    grub.release()
    return kernels_unused

def removeUnused(version):
    if not version or version not in listUnused():
        fail(FAIL_KERNEL_IN_USE % version)
    removeKernel(version)

def setEntry(title, os_type, root, kernel, initrd, options, default, index):
    grub = grubParser(GRUB_DIR, write=True, timeout=TIMEOUT)

    if not len(title):
        fail(FAIL_NOTITLE)

    entry = makeGrubEntry(title, os_type, root, kernel, initrd, options)

    if index == -1:
        grub.config.addEntry(entry)
    else:
        grub.config.entries[index] = entry

    if default == "yes":
        grub.config.setOption("default", index)
    elif default == "saved":
        grub.config.setOption("default", "saved")
        for index, entry in enumerate(grub.config.entries):
            entry.setCommand("savedefault", "")
    elif default == "no" and index != None:
        default_index = grub.config.getOption("default", "0")
        if default_index != "saved" and int(default_index) == index:
            grub.config.setOption("default", "0")

    grub.release()
    notify("Boot.Loader", "Changed", "entry")
