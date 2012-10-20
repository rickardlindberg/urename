#!/bin/sh
make
cp urename bin
git add bin/urename
git commit -m 'release'
