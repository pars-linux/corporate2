#/usr/bin/python

import os
import pisi

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if fromVersion <= "3.1":

        oldContribUrl = "http://paketler.pardus.org.tr/contrib-2007/pisi-index.xml.bz2"
        newContribUrl = "http://paketler.pardus.org.tr/contrib-2008/pisi-index.xml.bz2"
        repodb = pisi.db.repodb.RepoDB()

        if repodb.has_repo_url(oldContribUrl):
            for r in repodb.list_repos():
                if repodb.get_repo_url(r) == oldContribUrl:
                    pisi.api.remove_repo(r)
                    pisi.api.add_repo(r, newContribUrl )


