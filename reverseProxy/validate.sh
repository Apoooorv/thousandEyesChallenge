#!/bin/bash
FLAG='true'
ERROR=''
if [ -z "${TIMEOUT}" ]; then
  FLAG="false"
  ERROR="TIMEOUT"
fi

if [ -z "${THRESHOLD}" ]; then
  FLAG="false"
  ERROR=$ERROR",THRESHOLD"
fi

if [ -z "${MYSQL_DB}" ]; then
  FLAG="false"
  ERROR=$ERROR",MYSQLDB"
fi

if [ -z "${MYSQL_USER}" ]; then
  FLAG="false"
  ERROR=$ERROR",MYSQLUSER"
fi

if [ -z "${MYSQL_PASS}" ]; then
  FLAG="false"
  ERROR=$ERROR",MYSQLPASS"
fi

if [ -z "${MYSQL_HOST}" ]; then
  FLAG="false"
  ERROR=$ERROR",MYSQLHOST"
fi

if [ -z "${MYSQL_PORT}" ]; then
  FLAG="false"
  ERROR=$ERROR",MYSQLPORT"
fi

echo $FLAG

if [ $FLAG = "false" ]; then
  echo "Error. Please provide an environmental variables named: "$ERROR
  exit 1
else
  python /home/src/manage.py migrate statistics
  gunicorn --bind 0.0.0.0:8080 --access-logfile=/home/src/proxy.logs --pythonpath /home/src/ reverseProxy.wsgi
fi
