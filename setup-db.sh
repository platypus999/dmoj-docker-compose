#!/bin/bash
set -euxo pipefail

python3 manage.py migrate
python3 manage.py loaddata navbar
python3 manage.py loaddata language_small
python3 manage.py loaddata demo

# uwsgi --ini uwsgi.ini
python3 manage.py runserver 0.0.0.0:8000