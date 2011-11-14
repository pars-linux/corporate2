#!/bin/bash

BRANCH_NAME="mozilla-1.9.2"
RELEASE_TAG="FIREFOX_3_6_24_RELEASE"
VERSION="3.6.24"

# These are Pardus supported languages. This list may changed by time to time
LOCALES="be ca de es-AR es-ES fr hu it nl pl pt-BR sv-SE tr"

test ! -d l10n && mkdir l10n
for locale in $LOCALES
do
    hg clone http://hg.mozilla.org/releases/l10n-$BRANCH_NAME/$locale l10n/$locale
    [ "$RELEASE_TAG" == "default" ] || hg -R l10n/$locale up -C -r $RELEASE_TAG
done

tar cjf l10n-$VERSION.tar.bz2 --exclude=.hgtags --exclude=.hgignore --exclude=.hg l10n

