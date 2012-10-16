#!/bin/bash
set -e
WORK=/var/www/polls/mysite
OUT=/var/log/fastcgi/mysite.out.log
ERR=/var/log/fastcgi/mysite.err.log
exec /usr/bin/python /var/www/polls/mysite/manage.py runfcgi host=127.0.0.1 port=8080 workdir=$WORK outlog=$OUT errlog=$ERR daemonize=true
