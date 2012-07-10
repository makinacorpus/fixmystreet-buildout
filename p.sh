#!/usr/bin/env bash
cd $(dirname $0)
ps -axo pid,cmd,start_time,state|egrep "T$"|grep "bash ./p.sh"|grep -v grep|awk '{print $1}'|xargs kill -9
while true;do
     ps aux|grep bin/gunicorn_paster|awk '{print $2}'|xargs kill -9
     ps aux|grep bin/paster|awk '{print $2}'|xargs kill -9
     reset
     bin/paster serve --reload etc/wsgi/instance.ini
     #./bin/paster serve --reload etc/wsgi/instance.ini
     #./bin/paster serve etc/wsgi/instance.ini
     echo;echo;echo
     echo "--------------------------------------------------------------"
     echo "              Press enter to restart"
     echo "--------------------------------------------------------------"
     read
done           
# vim:set et sts=4 ts=4 tw=0:
