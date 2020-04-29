# django-easy-audit exception reproduction


## Setup

1. `virtualenv -p python3 venv`
1. `source venv/bin/activate`
1. `pip install -r requirements.txt`
1. `./manage.py migrate`
1. `./manage.py runserver`

This is a basic example. No configuration is needed. SQLite is used for the DB.