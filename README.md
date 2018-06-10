# あなろぐげーむまねーじゃー(仮)
とりあえず増えてきたボードゲームのリストとかを管理できる簡易Webアプリを作る。

## 条件
- Pythonで作る
- Django2.0で作る
- Pipenvを使ってみる
- Docker Composeで
- Arukasが使えればいいなー

## もろもろ

```
# ボリュームをマウントしてbashをたたく
$ docker run -it -v $(pwd):/code django /bin/bash

# ポートフォワーディングもしておきたい
$ docker run -it -p 8000:8000 -v $(pwd):/code django /bin/bash

# ゲストにて、pipenv環境セットアップしたらとりあえず動かしてみる
/code# pipenv run python manage.py runserver 0.0.0.0:8000
```
