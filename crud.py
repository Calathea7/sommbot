from model import db, User, Wine, Recommendation, DsrWine, Descriptor, connect_to_db


def all_wines():

  return Wine.query.all()

def get_wine_by_year(year):

  return Wine.query.filter(Wine.year == year).all()

def get_wine_by_price(price):

  return Wine.query.filter(Wine.price == price).all()

def get_wine_by_filters(args**):

  winedescr = db.session.query(Wine.wine_title, func.count(Descriptor.name)).join(Wine.descriptors)
  winefilt = winedescr.filter(Wine.year.between('2000', '2014'), Wine.price.between('20', '30'), Descriptor.name.in_(('cherry', 'strawberry', 'juicy')))
  winerec = winefilt.group_by(Wine.wine_title).order_by(desc(func.count(Descriptor.name))).limit(5).all()





if __name__ == '__main__':
    from server import app
    connect_to_db(app)
