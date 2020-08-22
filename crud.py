from model import db, User, Wine, Recommendation, DsrWine, Descriptor, connect_to_db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import joinedload
from sqlalchemy.sql import func
from sqlalchemy import desc

def create_user(email, password, name):

  user = User(email=email, password=password, name=name)

  db.session.add(user)
  db.session.commit()

  return user

def all_users():

  return User.query.all()

def get_user_by_email(email):

  return User.query.filter(User.email == email).first()

def all_wines():

  return Wine.query.all()

def get_wine_by_year(year):

  return Wine.query.filter(Wine.year == year).all()

def get_wine_by_price(price):

  return Wine.query.filter(Wine.price == price).all()

def get_wine_by_filters(min_year, max_year, min_price, max_price, descriptors):

  # winedescr = db.session.query(Wine.wine_title, func.count(Descriptor.name)).join(Wine.descriptors)
  # winefilt = winedescr.filter(Wine.year.between(min_year, max_year), Wine.price.between(min_year, max_year))
  # winefd = winefilt.filter(Descriptor.name.in_((descriptors)))
  # winerec = winefd.group_by(Wine.wine_title).order_by(desc(func.count(Descriptor.name))).limit(5).all()

  return db.session.query(Wine.wine_title, func.count(Descriptor.name)).join(Wine.descriptors).filter(Wine.year.between(min_year, max_year), Wine.price.between(min_price, max_price), Descriptor.name.in_((descriptors))).group_by(Wine.wine_title).order_by(desc(func.count(Descriptor.name))).limit(5).all()



if __name__ == '__main__':
    from server import app
    connect_to_db(app)
