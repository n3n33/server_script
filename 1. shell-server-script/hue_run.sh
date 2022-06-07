#!/usr/bin/env bash

usage() {
  echo "
usage: $0 <options>
  start: hue start
  stop: hue stop
  "
  exit 1
}

case $1 in
  start)
    echo "########hue start now########"
    echo "hue home -> /data2/hue-release-4.10.0"
    echo "hue logs" -> /data2/hue_running.log
    echo "/data2/hue-release-4.10.0/build/env/hue runserver 0.0.0.0:8000 >> /data2/hue_running.log 2>&1 &"
    nohup /data2/hue-release-4.10.0/build/env/hue runserver 0.0.0.0:8000 >> /data2/hue_running.log 2>&1 &
    ;;
  stop)
    echo "########hue stop now########"
    echo "hue process number"
    hue_ps=$(netstat -nltp | grep 8000 | awk '{{print $7}}'| cut -d '/' -f1)
    echo ${hue_ps}
    echo "kill hue"
    kill -9 ${hue_ps}
   ;;
  *)
    usage
    exit 1
    ;;
esac