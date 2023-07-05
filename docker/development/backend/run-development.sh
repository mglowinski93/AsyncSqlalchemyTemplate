#!/bin/bash
set -e

# Install python packages.
python -m pip install --upgrade --user --disable-pip-version-check pip
pip install -r /requirements/development.txt

cd ./persistence_layer
alembic upgrade head
cd ../

# Run the application.
python main.py
