#!/usr/bin/env bash

./tcp-port-wait.sh $JOB_HISTORY_DB_HOST $JOB_HISTORY_DB_PORT

if [ -f "./backup_to_restore.sql" ]
then
    echo "backup_to_restore.sql exists; restoring it"
    PGPASSWORD=$JOB_HISTORY_DB_PASSWORD psql -U $JOB_HISTORY_DB_USERNAME -d $JOB_HISTORY_DB_NAME -h $JOB_HISTORY_DB_HOST -p $JOB_HISTORY_DB_PORT < ./backup_to_restore.sql
fi
./manage.py migrate --no-input

mkdir -p $JOB_HISTORY_STATIC_ROOT
./manage.py collectstatic --no-input

exec "$@"
