falcon example
===


falconを使ったWeb APIサーバのサンプル

* Python 3.5.1
* falcon
* gunicorn
* SQLAlchemy

※ライブラリのバージョンは [requirements.txt](./requirements.txt)を参照


環境構築から疎通確認まで
---

1. `git clone`
1. `cd python3_falcon_example`
1. `pyenv virtualenv 3.5.1 py-falcon`
1. `pyenv local py-falcon`
1. `pip install -r requirements.txt`
  * `pip install falcon`
  * `pip install gunicorn` 
1. `cd api && gunicorn routes:api`
1. `curl localhost:8000`



POSTのテスト
`curl -w '\n' 'http://localhost:8000/' --data '{"name":"test","task":"task-test"}' -XPOST`




参考
https://impythonist.wordpress.com/2015/09/12/build-massively-scalable-restful-api-with-falcon-and-pypy/
http://qiita.com/yasuhiroki/items/a569d3371a66e365316f
http://qiita.com/makaaso/items/ed00398f1caa9dd83bc7


https://github.com/brandoncazander/pendulum
ディレクトリやファイル構成が参考になりそう


https://github.com/pglass/digaas/blob/066ee26f805cfc58f8353d97a9999b5d0b906b1a/digaas/models.py

http://sbox.hatenablog.jp/entry/2012/03/09/071051

https://github.com/davehalladay/openr-flask-api/blob/45a52b4ca04c63895550653f2e2676a875bad489/models/user.py
https://github.com/davehalladay/openr-flask-api/blob/45a52b4ca04c63895550653f2e2676a875bad489/database.py