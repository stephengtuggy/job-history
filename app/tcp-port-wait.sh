#!/bin/sh

set -e

if [ -z "$1" ] || [ -z "$2" ]
then
    echo "tcp-port-wait - block until specified TCP port becomes available"
    echo "Usage: tcp-port-wait HOST PORT"
    exit 1
fi
echo Waiting for port "$1":$2 to become available...
while ! nc -z "$1" $2 2>/dev/null
do
    elapsed=$elapsed+1
    if [ "$elapsed" -gt 90 ] 
    then
        echo "TIMED OUT !"
        exit 1
    fi  
    sleep 1;
done

echo "READY !"
