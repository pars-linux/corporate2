# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "PulseAudio system sound daemon",
                 "tr": "PulseAudio ses servisi"})
serviceDefault = "off"
serviceConf = "pulseaudio"

MSG_ERR_PLSEGRPNOTFOND = _({"en": "No pulse-access group found in system, exiting.",
                            "tr": "Sistende pulse-access grubu bulunamadı, çıkılıyor.",
                            })
MSG_ERR_PLSENOTMEMB = _({"en": "The following users are not a member of the pulse-access group: %s",
                         "tr": "Şu kullanıcılar pulse-access grubunun üyesi değil: %s",
                         })
MSG_ERR_PLSENOTSYSTMODE = _({"en": "Adjust the settings in /etc/conf.d/pulseaudio for running PulseAudio in system mode.",
                             "tr": "PulseAudio'yu sistem kipinde çalıştırmak için /etc/conf.d/pulseaudio dosyasında ayar yapmalısınız.",
                             })
MSG_ERR_PLSEINPERUSER = _({"en": "PulseAudio is running in per-user mode, you can't stop it using 'service'.",
                           "tr": "PulseAudio kullanıcı kipinde çalışıyor, 'service' komutuyla durduramazsınız.",
                           })

startup_type = config.get("PULSE_SERVER_TYPE")

def check_credentials():
    # In order to run PA in system-wide mode, all users should be a member
    # of the pulse-access group.
    import pwd
    import grp

    pulse_access_users = []
    try:
        pulse_access_users = grp.getgrnam("pulse-access")[3]
    except KeyError:
        # Group not found
        raise KeyError
        return

    users = []

    for user in pwd.getpwall():
        # We're searching for the regular users
        if user[2] >= 1000 and user[2] < 65534:
            if user[0] not in pulse_access_users:
                users.append(user[0])

    return users

@synchronized
def start():
    if startup_type == "system":
        # Launch system-wide PulseAudio daemon
        users = None
        try:
            users = check_credentials()
        except KeyError:
            fail(MSG_ERR_PLSEGRPNOTFOND)

        if users:
            fail(MSG_ERR_PLSENOTMEMB % ",".join(users))
        else:
            startService(command="/usr/bin/pulseaudio",
                         args=config.get("PULSE_SYSTEM_ARGS", ""),
                         detach=True)
    else:
        fail(MSG_ERR_PLSENOTSYSTMODE)

@synchronized
def stop():
    if startup_type == "system":
        pass
    elif startup_type == "personal":
        fail(MSG_ERR_PLSEINPERUSER)

def status():
    return isServiceRunning(command="/usr/bin/pulseaudio")
