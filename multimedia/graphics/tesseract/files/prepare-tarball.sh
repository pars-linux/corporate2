#!/bin/bash

LANGS="2.00.deu 2.01.por 2.00.nld 2.00.spa 2.00.ita 2.00.fra 2.00.eng"

# Pass the version as parameter
wget http://tesseract-ocr.googlecode.com/files/tesseract-$1.tar.gz

tar xvzf tesseract-$1.tar.gz
cd tesseract-$1

# Fix permissions
find -name "*.cpp" | xargs chmod -x
find -name "*.h" | xargs chmod -x
find -type d | xargs chmod 755

# Get language packs
cd tessdata

for lang in $LANGS; do
    echo "Downloading tesseract-$lang.tar.gz.."
    wget http://tesseract-ocr.googlecode.com/files/tesseract-$lang.tar.gz
    tar xvzf tesseract-$lang.tar.gz
    rm -rf *.tar.gz
done

chmod -R 644 tessdata/*
cp tessdata/* .
rm -rf tessdata

cd ../../
rm -rf *.tar.gz

tar cvjf tesseract-$1.tar.bz2 tesseract-$1
sha1sum *.bz2
