#%PAM-1.0

auth       include      system-auth
auth       required     pam_nologin.so

account    include      system-auth

password   include      system-auth

session    include      system-auth
