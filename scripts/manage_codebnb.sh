#!/usr/bin/env bash

export WORKON_HOME=/var/envs
export PROJECT_HOME=/var/www
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_HOOK_DIR=/var/envs/bin
export PIP_RESPECT_VIRTUALENV=true
export COMPANIFY_MODE=codebnb

source /var/envs/companify/bin/activate

cd /var/www/subdomains/codebnb/companify_api/public_html/

python manage.py "$@"
