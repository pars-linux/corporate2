#!/bin/bash

BRANCH=$1

if [ ! -d fedora-kernel ]; then
    fedora kernel
fi

cd fedora-kernel
git checkout origin/$BRANCH/master

cat kernel.spec | egrep "^ApplyPatch.*\..*" > patches
vi patches # filter

for patch in `gawk '{print $2}' patches`; do
    \cp $patch ../files/fedora
done

rm -rf patches

