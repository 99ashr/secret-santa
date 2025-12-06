#!/usr/bin/env bash
# Start script for Render — ensures correct gunicorn invocation
set -euo pipefail

# Use PORT provided by Render (default 8000 for local testing)
: ${PORT:=8000}

echo "Starting gunicorn with PORT=${PORT}"

exec gunicorn secret_santa_config.wsgi:application --bind 0.0.0.0:${PORT} --workers 3
