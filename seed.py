from models import db, User
from app import db;

db.drop_all()
db.create_all()

rando = User.signup(username="rando",pwd='cat',email="rando@gmail.com")


db.session.add(rando)
db.session.commit()

