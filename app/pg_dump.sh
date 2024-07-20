#!/bin/sh

PGPASSWORD="$JOB_HISTORY_DB_PASSWORD" pg_dump --file=backup_to_restore.sql --format=p --clean --encoding=utf8 --if-exists --dbname="$JOB_HISTORY_DB_NAME" --host="$JOB_HISTORY_DB_HOST" --port=$JOB_HISTORY_DB_PORT --username="$JOB_HISTORY_DB_USERNAME"
