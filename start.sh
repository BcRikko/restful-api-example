#! /bin/sh

# nginx起動
sudo /etc/init.d/nginx start

# gunicorn起動
ROOT=/api
API=route:api

cd $ROOT
sudo gunicorn -c $ROOT/gunicorn.conf.py $API