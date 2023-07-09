#!/bin/bash
set -e

# Install python packages.
python -m pip install --upgrade --user --disable-pip-version-check pip
pip install -r /requirements/tests.txt

# Wait for the database to be ready.
/tools/wait-for "${DATABASE_HOST}":"${DATABASE_PORT}" -t 60
if [ $? -ne 0 ]; then
    echo Receipt of readiness from database failed. Exiting...
    exit 1
fi
sleep 5 # Wait to be sure, that database is up.

# Run database migrations.
cd ./persistence_layer
alembic upgrade head
cd ../

# Run the application.
pytest
