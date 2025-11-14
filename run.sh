#!/usr/bin/env bash

export DJANGO_PORT=9505
export DJANGO_HOST="192.168.0.140"

if [ "$1" ]; then
    echo "found first parameter"
    export DJANGO_PORT="$1"
fi

if [ "$2" ]; then
    echo "found first parameter"
    export DJANGO_HOST="$2"
fi

echo "DJANGO_PORT is $DJANGO_PORT" 
echo "DJANGO_HOST is $DJANGO_HOST"

./manage.py runserver $DJANGO_HOST:$DJANGO_PORT
