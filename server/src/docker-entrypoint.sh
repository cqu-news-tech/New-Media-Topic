#!/bin/sh
set -e
exec gunicorn api:app -c ./gunicorn.conf