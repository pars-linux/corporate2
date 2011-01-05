#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown -R postgres:postgres /var/lib/pgsql")
    os.system("/bin/chmod -R 0700 /var/lib/pgsql/data")
    os.system("/bin/chmod -R 0700 /var/lib/pgsql/backups")

    # On first install...
    if not os.path.exists("/var/lib/pgsql/data/base"):
        os.system('/bin/su postgres -s /bin/sh -p -c "/usr/bin/initdb --pgdata /var/lib/pgsql/data"')
