from model import db, User, Wine, Recommendation, DsrWine, Descriptor, connect_to_db


def all_wines():

  return Wine.query.all()

def get_wine_by_year(year):

  return Wine.query.filter(Wine.year == year).all()

def get_wine_by_price(price):

  return Wine.query.filter(Wine.price == price).all()





if __name__ == '__main__':
    from server import app
    connect_to_db(app)
