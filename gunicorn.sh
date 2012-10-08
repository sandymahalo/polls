#!/bin/bash
set -eLOGFILE=/var/log/gunicorn/polls.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
USER=deploy
GROUP=deploy
cd /var/www/polls
source ../bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec ../bin/gunicorn_django -w $NUM_WORKERS \--user=$USER --group=$GROUP --log-level=debug \--log-file=$LOGFILE 2>>$LOGFILE
