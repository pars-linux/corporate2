if [ $LC_ALL = tr_TR.UTF-8 -a -x /usr/bin/zpspell ]; then
    echo "KSpell_Client=3"
else
    echo "KSpell_Client=1"
fi

echo "KSpell_Encoding=11"
