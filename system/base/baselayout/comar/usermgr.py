# -*- coding: utf-8 -*-
#
# Copyright (C) 2006-2010 TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#

import os
import glob
import fcntl
import random
import shutil
import hashlib

import libuser

from string import ascii_letters, digits
from pardus.fileutils import FileLock

try:
    import polkit
except ImportError:
    pass


# faces

FACES = [
    "/usr/kde/3.5/share/apps/kdm/pics/users",
]

# messages

invalid_username_msg = {
    "en": "User name is invalid.",
    "tr": "Kullanıcı adı geçersiz.",
    "fr": "Nom d'utilisateur invalide.",
    "es": "Nombre de usuario no es válido.",
    "de": "Benutzername nicht erlaubt.",
    "nl": "Gebruikernaam is ongeldig.",
}

invalid_realname_msg = {
    "en": "Real name is invalid.",
    "tr": "Gerçek isim geçersiz.",
    "fr": "Nom réel invalide.",
    "es": "Nombre real no es válido.",
    "de": "Dieser vollständige Name ist nicht erlaubt.",
    "nl": "Echte naam is ongeldig.",
}

short_password_msg = {
    "en": "Password is too short.",
    "tr": "Parola çok kısa.",
    "fr": "Mot de passe trop court.",
    "es": "Contraseña es demadiado corta.",
    "de": "Passwort ist zu kurz.",
    "nl": "Wachtwoord is te kort.",
}

name_password_msg = {
    "en": "Dont use your name as a password.",
    "tr": "Adınızı parola olarak kullanmayın.",
    "fr": "N'utilisez pas votre nom comme mot de passe.",
    "es": "No use su nombre como contraseña.",
    "de": "Benutzen Sie nicht Ihren Namen als Passwort.",
    "nl": "Uw naam niet als wachtwoord gebruiken.",
}

invalid_group_msg = {
    "en": "Invalid group name:",
    "tr": "Geçersiz grup adı:",
    "fr": "Nom de groupe invalide:",
    "es": "Nombre de grupo inválido:",
    "de": "Gruppenname nicht erlaubt:",
    "nl": "Ongeldige groepnaam:",
}

invalid_userid_msg = {
    "en": "Invalid user ID.",
    "tr": "Geçersiz kullanıcı numarası.",
    "fr": "Identifiant utilisateur invalide.",
    "es": "ID de usuario no válido.",
    "de": "User-ID nicht erlaubt.",
    "nl": "Gebruiker-id is ongeldig.",
}

used_userid_msg = {
    "en": "This user ID is already used.",
    "tr": "Bu kullanıcı numarası zaten kullanılmakta.",
    "fr": "Cet identifiant utilisateur est déjà utilisé.",
    "es": "Este ID de usuario ya está en uso.",
    "de": "Dieser user-ID is schon vergeben.",
    "nl": "Deze gebruiker-id is reeds in gebruik.",
}

used_username_msg = {
    "en": "This user name is already used.",
    "tr": "Bu kullanıcı adı zaten kullanılmakta.",
    "fr": "Ce nom d'utilisateur est déjà utilisé.",
    "es": "Este nombre de usuario ya está en uso.",
    "de": "Dieser Benutzername is schon vergeben.",
    "nl": "Deze gebruikernaam is reeds in gebruik.",
}

no_group_msg = {
    "en": "No such group exists.",
    "tr": "Böyle bir grup yok.",
    "fr": "Il n'existe aucun groupe de ce nom-là.",
    "es": "No existe el grupo.",
    "de": "Diese Gruppe gibt es nicht.",
    "nl": "Deze groep bestaat niet.",
}

no_user_msg = {
    "en": "No user with given ID.",
    "tr": "Verilen numaralı bir kullanıcı yok.",
    "fr": "Il n'existe aucun utilisateur avec et identifiant.",
    "es": "No existe usuario con éste ID.",
    "de": "Es gibt keien Benutzer mit dem angegebenen ID.",
    "nl": "Gebruiker met opgegeven ID bestaat niet.",
}

delete_root_msg = {
    "en": "You cant delete root user.",
    "tr": "Kök kullanıcıyı silemezsiniz.",
    "fr": "Vous ne pouvez pas supprimer l'administrateur.",
    "es": "No se puede eliminar al usuario root.",
    "de": "Benutzer ROOT darf nicht gelöscht werden.",
    "nl": "Systeembeheerder (root) kan niet verwijderd worden.",
}

invalid_groupid_msg = {
    "en": "Invalid group ID.",
    "tr": "Geçersiz grup numarası.",
    "fr": "Identifiant de groupe invalide.",
    "es": "ID del grupo inválido.",
    "de": "Gruppen-ID nicht zulässig.",
    "nl": "Groep-ID is ongeldig.",
}

used_groupid_msg = {
    "en": "This group ID is already used.",
    "tr": "Bu grup numarası zaten kullanılmakta.",
    "fr": "Cet identifiant de groupe est déjà utilisé.",
    "es": "Este ID de grupo ya está en uso.",
    "de": "Dieser Gruppen-ID is schon vergeben.",
    "nl": "Deze groep-ID is reeds in gebruik.",
}

used_groupname_msg = {
    "en": "This group name is already used.",
    "tr": "Bu grup adı zaten kullanılmakta.",
    "fr": "Ce nom de groupe est déjà utilisé.",
    "es": "Este nombre de grupo ya está en uso.",
    "de": "Dieser Gruppennam is schon vergeben.",
    "nl": "Deze groepnaam is reeds in gebruik.",
}

# parameters
uid_minimum = 1000
uid_maximum = 65000

#

admin = libuser.admin()

def setFace(uid, homedir):
    files = []
    for directory in FACES:
        if os.path.exists(directory):
            for filename in os.listdir(directory):
                if filename.endswith(".png"):
                    files.append(os.path.join(directory, filename))
    if len(files):
        icon = os.path.join(homedir, ".face.icon")
        shutil.copy(random.choice(files), icon)
        os.chmod(icon, 0644)
        os.chown(icon, uid, 100)

def checkName(name):
    first_valid = ascii_letters
    valid = ascii_letters + "_-" + digits
    if len(name) == 0 or len(filter(lambda x: not x in valid, name)) != 0 or not name[0] in first_valid:
        fail(_(invalid_username_msg))

def checkRealName(realname):
    if len(filter(lambda x: x == "\n" or x == ":", realname)) != 0:
        fail(_(invalid_realname_msg))

def checkPassword(password, badlist):
    if len(password) < 4:
        fail(_(short_password_msg))
    if password in badlist:
        fail(_(name_password_msg))

def checkGroupName(name):
    valid = ascii_letters + "_-"
    if name == "" or len(filter(lambda x: not x in valid, name)) != 0:
        fail(_(invalid_group_msg) + " " + name)

#

class User:
    def __init__(self):
        self.password = None

    def __str__(self):
        return "%s (%d, %d)\n  %s\n  %s\n  %s\n  %s" % (
            self.name, self.uid, self.gid,
            self.realname, self.homedir, self.shell,
            self.password
        )


class Group:
    def __str__(self):
        s = "%s (%d)" % (self.name, self.gid)
        for name in self.members:
            s += "\n %s" % name
        return s

# methods

def userList():
    user_list = []
    users = admin.enumerateUsersFull()
    for user in users:
        if libuser.UIDNUMBER not in dict(user):
            continue
        user_list.append((int(user[libuser.UIDNUMBER][0]), user[libuser.USERNAME][0], user[libuser.GECOS][0]))
    return user_list


def userInfo(uid):
    user = admin.lookupUserById(uid)
    if user:
        groups = admin.enumerateGroupsByUser(user.get(libuser.USERNAME)[0])
        main = admin.lookupGroupById(user.get(libuser.GIDNUMBER)[0])
        mainGroupName = main.get(libuser.GROUPNAME)[0]
        if mainGroupName in groups:
            groups.remove(mainGroupName)
            groups.insert(0, mainGroupName)
        ret=(
            user.get(libuser.USERNAME)[0],
            user.get(libuser.GECOS)[0],
            int(user.get(libuser.GIDNUMBER)[0]),
            user.get(libuser.HOMEDIRECTORY)[0],
            user.get(libuser.LOGINSHELL)[0],
            groups,
            )
    else:
        fail(_(no_user_msg))

    return ret


def addUser(uid, name, realname, homedir, shell, password, groups, grants, blocks):
    checkName(name)
    usrCtrl = admin.lookupUserByName(name)
    if usrCtrl:
        fail(_(used_username_msg))

    new_user = admin.initUser(name)

    if not uid == -1:
        try:
            if uid < 0 or uid > 65536:
                raise
        except:
            fail(_(invalid_userid_msg))
        usrCtrl = admin.lookupUserById(uid)
        if usrCtrl:
            fail(_(used_userid_msg))
        new_user.set(libuser.UIDNUMBER, uid)
    if realname:
        checkRealName(realname)
        new_user.set(libuser.GECOS, realname)
    if homedir:
        new_user.set(libuser.HOMEDIRECTORY, homedir)
    if shell:
        new_user.set(libuser.LOGINSHELL, shell)
    if password:
        checkPassword(password, (name, realname))
        new_user.set(libuser.SHADOWPASSWORD, shadowCrypt(password))
    if len(groups) == 0:
        groups.append("nogroup")
    print groups
    for item in groups:
        checkGroupName(item)
        gr = admin.lookupGroupByName(item)
        if gr:
            addUserToGroup(new_user, gr)
    # First group in the list is the user's main group
    g = admin.lookupGroupByName(groups[0])
    new_user.set(libuser.GIDNUMBER, g.get(libuser.GIDNUMBER))

    for grant in grants:
        if grant != "":
            grantAuthorization(uid, grant)
    for block in blocks:
        if block != "":
            blockAuthorization(uid, block)

    try:
        admin.addUser(new_user, True, False)
    except Exception, e:
        print e

    return int(new_user[libuser.UIDNUMBER][0])

def addUserToGroup(user, group):
    members = group.get(libuser.MEMBERNAME)
    if not members:
        members = []
    members.append(user.get(libuser.USERNAME)[0])
    group.set(libuser.MEMBERNAME, members)
    admin.modifyGroup(group)

def setUser(uid, realname, homedir, shell, password, groups):
    user = admin.lookupUserById(uid)
    print groups
    if user:
        username = user.get(libuser.USERNAME)[0]
        if realname:
            checkRealName(realname)
            user.set(libuser.GECOS, realname)
        if homedir:
            user.set(libuser.HOMEDIRECTORY, homedir)
        if shell:
            user.set(libuser.LOGINSHELL, shell)
        if password:
            checkPassword(password, (username, user.get(libuser.GECOS)[0], realname))
            user.set(libuser.SHADOWPASSWORD, shadowCrypt(password))
        if groups:
            # FIXME: check main group
            for old in admin.enumerateGroupsByUser(username):
                if old not in groups:
                    deleteUserFromGroup(user, admin.lookupGroupByName(old))

            for item in groups:
                checkGroupName(item)
                gr = admin.lookupGroupByName(item)
                if username not in admin.enumerateGroupsByUser(username):
                    addUserToGroup(user, gr)

            # First group in the list is the user's main group
            g = admin.lookupGroupByName(groups[0])
            user.set(libuser.GIDNUMBER, g.get(libuser.GIDNUMBER))

        admin.modifyUser(user)
    else:
        fail(_(no_user_msg))


def deleteUser(uid, deletefiles):
    if uid == 0:
        fail(_(delete_root_msg))
    user = admin.lookupUserById(int(uid))
    if user:
        #delete authorizations of user
        try:
            polkit.auth_revoke_all(uid)
        except:
            pass
        for gr in admin.enumerateGroupsByUser(user.get(libuser.USERNAME)[0]):
            group = admin.lookupGroupByName(gr)
            deleteUserFromGroup(user, group)

        admin.deleteUser(user, deletefiles, False)
    else:
        fail(_(no_user_msg))

def deleteUserFromGroup(user, group):
    members = group.get(libuser.MEMBERNAME)
    if members:
        members.remove(user.get(libuser.USERNAME)[0])
        group.set(libuser.MEMBERNAME, members)
        admin.modifyGroup(group)

def groupList():
    group_list=[]
    groups = admin.enumerateGroupsFull()
    for group in groups:
        group_list.append((int(group[libuser.GIDNUMBER][0]), group[libuser.GROUPNAME][0]))
    return group_list


def addGroup(gid, name):
    new_group = admin.initGroup(name)

    if not gid == -1:
        if gid < 0 or gid > 65536:
            fail(_(invalid_groupid_msg))
        if admin.lookupGroupById(gid):
            fail(_(used_groupid_msg))
        new_group[libuser.GIDNUMBER] = gid

    if admin.lookupGroupByName(name):
        fail(_(used_groupname_msg))

    admin.addGroup(new_group)

    return int(new_group[libuser.GIDNUMBER][0])

def deleteGroup(gid):
    group = admin.lookupGroupById(gid)
    if group:
        admin.deleteGroup(group)
    else:
        fail(_(invalid_groupid_msg))


#
# Crypt function for shadow file
#

def shadowCrypt(password):
    des_salt = list('./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    salt, magic = str(random.random())[-8:], '$1$'

    ctx = hashlib.md5(password)
    ctx.update(magic)
    ctx.update(salt)

    ctx1 = hashlib.md5(password)
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
        ctx1 = hashlib.md5()
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

#
# List authorizations by UID
#

def listUserAuthorizations(uid):
    actions = polkit.auth_list_uid(int(uid))
    auths = []
    for action in actions:
        action_info = polkit.action_info(action['action_id'])
        auths.append((action['action_id'], action['scope'], action_info['description'], action_info['policy_active'], action['negative']))
    return auths

def listUserAuthorizationsByCategory(uid, name):
    actions = polkit.auth_list_uid(int(uid))
    auths = []
    names = name.split('|')
    for action in actions:
        nameExist = False
        for nm in names:
            if action['action_id'].startswith(nm):
                nameExist = True
                break
        if nameExist:
            action_info = polkit.action_info(action['action_id'])
            auths.append((action['action_id'], action['scope'], action_info['description'], action_info['policy_active'], action['negative']))
    return auths

def getNegativeValue(uid, aid):
    """
     -1 : nothing found
      0 : blocked
      1 : granted
    """
    actions = polkit.auth_list_uid(int(uid))
    for action in actions:
        if aid == action['action_id']:
            if action['negative']:
                return 0
            else:
                return 1
    return -1

#
# Grant authorization to user
#

def grantAuthorization(uid, action):
    uid = int(uid)
    if action == "*":
        for action_id in polkit.action_list():
            try:
                polkit.auth_revoke(uid, action_id)
                polkit.auth_add(action_id, polkit.SCOPE_ALWAYS, uid)
            except:
                return False
    else:
        try:
            polkit.auth_revoke(uid, action)
            polkit.auth_add(action, polkit.SCOPE_ALWAYS, uid)
        except:
            return False
    return True

#
# Revoke authorization of user
#

def revokeAuthorization(uid, action):
    uid = int(uid)
    if action == "*":
        for action_id in polkit.action_list():
            try:
                polkit.auth_revoke(uid, action_id)
            except:
                return False
    else:
        try:
            polkit.auth_revoke(uid, action)
        except:
            return False
    return True

#
# Block authorization of user
#

def blockAuthorization(uid, action):
    uid = int(uid)
    if action == "*":
        for action_id in polkit.action_list():
            try:
                polkit.auth_revoke(uid, action_id)
                polkit.auth_block(uid, action_id)
            except:
                return False
    else:
        try:
            polkit.auth_revoke(uid, action)
            polkit.auth_block(uid, action)
        except:
            return False
    return True
