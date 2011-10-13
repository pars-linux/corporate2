#!/bin/bash

BRANCH_NAME="mozilla-1.9.2"
RELEASE_TAG="FIREFOX_3_6_23_RELEASE"
VERSION="3.6.23"

test ! -d mozilla && mkdir mozilla
hg clone http://hg.mozilla.org/releases/$BRANCH_NAME mozilla
pushd mozilla
[ "$RELEASE_TAG" == "default" ] || hg update -r $RELEASE_TAG
popd

tar cjf firefox-source-$VERSION.tar.bz2 --exclude=.hgtags --exclude=.hgignore --exclude=.hg --exclude=CVS mozilla

