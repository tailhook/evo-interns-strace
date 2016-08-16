#!/bin/sh

while true; do
    if [ -f app/.vagga/py/etc/hosts ]; then
        chmod a+rw app/.vagga/py/etc/hosts
        echo '127.0.0.2 localhost' > app/.vagga/py/etc/hosts
    fi
    ( cd screws;
      ${VAGGA:-vagga} redis-cli set visitors $((RANDOM % 65536)) > /dev/null)
    sleep 1
done
