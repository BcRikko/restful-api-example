#! /bin/sh

# nginx.confを/etc/nginx/conf.d/配下に移動する（`conf.d/*.conf`が設定ファイルとして読み込まれる）
sudo cp ./nginx.conf /etc/nginx/conf.d/