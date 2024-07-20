# Abort the entire script if an error occurs
set -e

# Next, run any pending database migrations
./manage.py migrate --no-input

# Collect Django static files...
mkdir -p "$JOB_HISTORY_STATIC_ROOT"
./manage.py collectstatic --no-input

# ... And last but not least, run whatever command was passed in to us
exec "$@"
