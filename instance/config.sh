#!/bin/bash

# service settings
export SHORTIFY_DEBUG=0
export SHORTIFY_PORT=80

# rdbms settings
export SHORTIFY_SQL_DBMS=postgresql
export SHORTIFY_SQL_USERNAME=postgres
export SHORTIFY_SQL_PASSWORD=##anubhav02##
export SHORTIFY_SQL_HOST=localhost
export SHORTIFY_SQL_PORT=5432
export SHORTIFY_SQL_DATABASE=url_shortener

# redis settings
export SHORTIFY_REDIS_HOST=localhost
export SHORTIFY_REDIS_PORT=6379
export SHORTIFY_REDIS_DB=0