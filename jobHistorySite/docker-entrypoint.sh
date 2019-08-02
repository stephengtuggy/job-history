#!/bin/bash

./tcp-port-wait.sh 0.0.0.0 $JOB_HISTORY_DB_PORT

# if [ -f "backup_to_restore.sql" ]

# fi
./manage.py migrate

mkdir -p $JOB_HISTORY_STATIC_ROOT
# ???
./manage.py collectstatic

# Replace eventually with execution of $@ ?
./manage.py runserver 0.0.0.0:8000
