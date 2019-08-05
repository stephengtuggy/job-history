#!/usr/bin/env bash

# Abort the entire script if an error occurs
set -e

# Wait for the db (postgres) container to be ready
./tcp-port-wait.sh $JOB_HISTORY_DB_HOST $JOB_HISTORY_DB_PORT

# Give it a little extra time, in case it has to create the database
sleep 2;

# If there's a database backup to restore, retore it
if [ -f "./backup_to_restore.sql" ]
then
    echo "backup_to_restore.sql exists; restoring it"
    PGPASSWORD=$JOB_HISTORY_DB_PASSWORD psql -U $JOB_HISTORY_DB_USERNAME -d $JOB_HISTORY_DB_NAME -h $JOB_HISTORY_DB_HOST -p $JOB_HISTORY_DB_PORT < ./backup_to_restore.sql
fi

# Next, run any pending database migrations
./manage.py migrate --no-input

# Collect Django static files...
mkdir -p $JOB_HISTORY_STATIC_ROOT
./manage.py collectstatic --no-input

# ... And last but not least, run whatever command was passed in to us
exec "$@"
