from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "%?gdb56vf873%"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def Homepage():
    """View homepage."""

    return render_template('root.html')

@app.route('/api/create-account', methods=["POST"])
def create_account():

  data = request.get_json()

  email = data["email"]
  password = data["password"]
  name = data["name"]

  user = crud.get_user_by_email(email=email)

  if user:
    status = 'error'
    message = 'Account with this email already exists. Please try logging in.'

  else:
    crud.create_user(email=email, password=password, name=name)
    status = 'success'
    message = 'Thank you for creating an account. Please log in.'

  return jsonify({'status': status, 'message': message})

@app.route('/api/login', methods=["POST"])
def login_user():

  data = request.get_json()

  email = data["email"]
  password = data["password"]

  user = crud.get_user_by_email_password(email=email, password=password)

  if user:
    status = 'success'
    message = 'You have successfully logged in!'

  else:
    status = 'error'
    message = 'Your email or password are incorrect'

  return jsonify({'status': status, 'message': message})

@app.route('/api/logout', methods=["GET", "POST"])
def logout_user():

  pass

  return None

@app.route('/api/user-profile', methods=["POST"])
def user_profile():

  data = request.get_json()

  return None


@app.route('/api/recommendation', methods=["POST"])
def recommendation():
  # print("hitting the rec route \n \n \n")
  # print(request.get_json())

  data = request.get_json()

  min_year = data["min_year"]
  max_year = data["max_year"]
  min_price = data["min_price"]
  max_price = data["max_price"]
  descriptors = data["descriptor"]

  wines = crud.get_wine_by_filters(min_year, max_year, min_price, max_price, descriptors)

  results = [wine[0] for wine in wines]


  return jsonify(results)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)





