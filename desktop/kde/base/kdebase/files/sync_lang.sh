# Set LC_ALL and LANG variables for non-KDE applications.

KDE_LANGUAGE=`kreadconfig --group Locale --key Language | cut -d: -f1`

if [ -n "$KDE_LANGUAGE" ]; then
    LC_ALL=`python -c "from pardus import localedata; print localedata.languages.get('$KDE_LANGUAGE', localedata.languages['en']).locale"`
    LANG=$LC_ALL
    export LC_ALL LANG
fi
