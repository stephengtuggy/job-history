#!/bin/bash

./tcp-port-wait.sh $JOB_HISTORY_DB_HOST $JOB_HISTORY_DB_PORT

# if [ -f "backup_to_restore.sql" ]

# fi
./manage.py migrate --no-input

mkdir -p $JOB_HISTORY_STATIC_ROOT
# ???
./manage.py collectstatic --no-input

# Replace eventually with execution of $@ ?
./manage.py runserver 0.0.0.0:8000
