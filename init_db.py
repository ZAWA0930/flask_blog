from blog import db
from blog.models import User

db.drop_all()
db.create_all()

print('A')


user1=User(email="zawazawagold4649@gmail.com", username="zawa", password="Taichi", administrator="1")
user2=User(email="AdminUser@admin.com", username="Administrator", password="Admin", administrator="1")


db.session.add(user1)
db.session.add(user2)
db.session.commit()
