#!/bin/sh
gunicorn -w 4 --threads 2 -b 0.0.0.0:5000 --chdir ldap_service "app:create_app()"