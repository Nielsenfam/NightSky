#!/bin/sh

case "$1" in
  start)
    echo "Starting Night Sky"
    /home/pi/bin/LEDgridDrive.py &
    ;;
  stop)
    echo "Stopping Night Sky"
    killall LEDgridDrive.py
    ;;
  *)
    echo "Usage: /etc/init.d/nightsky.sh"
    exit 1
    ;;
esac

exit 0
