#!/bin/bash
set -euxo pipefail

tables=$(echo "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'dmoj'" | python3 manage.py dbshell -- -N)
if [ "$tables" -eq 0 ]; then
    python3 manage.py migrate
    python3 manage.py loaddata navbar
    python3 manage.py loaddata language_small
    python3 manage.py loaddata demo
    python3 manage.py addjudge $JUDGE_NAME $JUDGE_KEY
fi

python3 manage.py runserver 0.0.0.0:8000