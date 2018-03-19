test Development Guide

For apache configuration

    sudo apt-get install libapache2-mod-wsgi-py3

Development setup

Install required system packages:

    sudo apt-get install python3-pip
    sudo apt-get install python3-dev python3-setuptools
    sudo apt-get install libpq-dev
    sudo apt-get install postgresql postgresql-contrib

Create www directory where project sites and environment dir

    mkdir /var/www && mkdir /var/envs && mkdir /var/envs/bin

Install virtualenvwrapper

    sudo pip3 install virtualenvwrapper
    sudo pip3 install --upgrade virtualenv

Add these to your bashrc virutualenvwrapper work

    export WORKON_HOME=/var/envs
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    export PROJECT_HOME=/var/www
    export VIRTUALENVWRAPPER_HOOK_DIR=/var/envs/bin    
    source /usr/local/bin/virtualenvwrapper.sh

Create virtualenv

    cd /var/envs && mkvirtualenv --python=/usr/bin/python3 test


Install requirements for a project.

    cd /var/www/test && pip install -r requirements/local.txt

    sudo chown :www-data /var/www/test_h
    sudo cp /var/www/test/test/conf/test.com.conf /etc/apache2/sites-available/
    sudo cp /var/www/test/test/wsgi_default.py /var/www/test/test/wsgi.py


##Database creation
###For psql

    sudo su - postgres
    psql > DROP DATABASE IF EXISTS test;
    psql > CREATE DATABASE test;
    psql > CREATE USER test_user WITH password 'hi48hc8wvntewczg9rk9v787qiye5iqx';
    psql > GRANT ALL privileges ON DATABASE test TO test_user;
    psql > ALTER USER test_user CREATEDB;

    
###For mysql

    mysql
    mysql > DROP DATABASE IF EXISTS test;
    mysql > CREATE DATABASE test CHARACTER SET utf8;
    mysql > CREATE USER 'test_user'@'localhost' IDENTIFIED BY 'hi48hc8wvntewczg9rk9v787qiye5iqx';
    mysql > GRANT ALL PRIVILEGES ON test.* TO 'test_user'@'localhost';

