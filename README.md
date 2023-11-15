# flaskを利用した簡易ブログサイト
flaskとBootstrapを使用した簡易ブログサイトを作成しました。
主に、flaskの練習用として作成しました。

# DEMO
サイトのレイアウトは以下の画像の通りです
![image](https://github.com/ZAWA0930/flask_practice/assets/93305831/f7bbf071-26e6-4210-accd-828c62c8a53b)


# Features
ユーザー登録することによってカテゴリとブログ投稿ができるようになり、投稿した記事は投稿したユーザーでしか編集できないようになっています。
また、ブログ管理者アカウントでログインするとユーザーの追加・削除などできるようになり、管理者しか見れないユーザー管理ページがあります。
パスワードはハッシュ化しているため、管理者にも表示されません。
# Requirement

flask==2.0.3
flask-wtf==0.15.1
flask_sqlalchemy==2.5.1
flask_migrate==3.1.0
flask_login==0.5.0
pytz==2021.3
pillow==9.0.1
werkzeug==2.0.3
wtforms==2.3.3
jinja2==3.0.3
email-validator==1.1.3
psycopg2==2.9.3
gunicorn==20.1.0
itsdangerous==2.1.2
markupSafe==2.1.1
click==8.0.4
requests==2.27.1
SQLAlchemy==1.4.39


# Note

今回はherokuを使用してデプロイしたため、PostgreSQLを使用した。画像を投稿するには、フリー画像等のリンクを使用しないといけない。
今後の改善点としてMySQLを使用してAWSからデプロイし、画像をファイルから投稿できるようにする。

# Author

* 作成者:ZAWA0930
* e-mail:zawazawagold4649@gmail.com


