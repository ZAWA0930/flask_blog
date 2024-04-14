# flaskを利用した簡易ブログサイト
flaskとBootstrapを使用した簡易ブログサイトを作成しました。
主に、flaskの練習用として作成しました。


https://zawa093flaskapp-ae8b269555e9.herokuapp.com/

諸事情によりherokuを利用できないため動作は以下のリンク
https://drive.google.com/file/d/1bBLSYgfPdz996NKcUABwEHeWzZf4-kRs/view?usp=sharing

# DEMO
サイトのレイアウトは以下の画像の通りです

![image](https://github.com/ZAWA0930/flask_blog/assets/93305831/49de8486-9df4-4cab-b3a7-8954760c93d7)


# Features
・ユーザー登録
・ログイン
・投稿
・カテゴリ登録
・ユーザー一覧
・検索バー
・管理者限定管理ページ
![ER](https://github.com/ZAWA0930/flask_blog/assets/93305831/c1d3ac98-fc51-4c14-bee9-dda7f8bc5d28)


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
今回、Flaskを使用して作成した理由はstreamlitでwebアプリに興味を持ちました。画像認識を使用するwebアプリを作成したいと考えたとき、pythonでできる小規模webアプリという条件にあてはまったのがFlaskでした。
制作期間は1か月半近くかかってしまいました。


反省点
今回はherokuを使用してデプロイしたため、PostgreSQLを使用した。画像を投稿するには、画像リンクを使用しないといけない。
今後の改善点としてCloudSQLやAWSからデプロイし、画像をファイルから投稿できるようにする。


# Author

* 作成者:ZAWA0930
* e-mail:zawazawagold4649@gmail.com


