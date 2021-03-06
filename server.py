from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import connect_to_db
import crud

app = Flask(__name__)
app.secret_key = "%?gdb56vf873%"

# login_manager = LoginManager()
# login_manager.init_app(app)

@app.route('/')
def Homepage():
    """View homepage."""

    return render_template('root.html')


# TODO: POST /api/user
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


# POST /api/user/login
# @ app.route('login
# @user_loader', methods=["POST"])
@app.route('/api/login', methods=["POST"])
def login_user():

  data = request.get_json()

  session['email'] = data["email"]
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

  if 'email' in session:
    session.pop('email', None)
    status = 'success'
    message = 'You have successfully logged out!'

  else:
    status = 'error'
    message = 'You were not logged in'

  return jsonify({'status': status, 'message': message})


# TODO: GET /api/user/<user_id>
@app.route('/api/user-profile', methods=["POST"])
def user_profile():

  data = request.get_json()

  return None

@app.route('/api/wine/save-rec')
def save_rec():

  data = request.get_json()

  rec_info = data["rec_info"]

  email = session['email']

  rec = crud.save_recommendation(rec_info=rec_info, user_email=email)

  if rec:
    status = 'success'
    message = 'Recommendation has been saved to your profile!'

  else:
    status = 'error'
    message = 'Something went wrong. Please try saving again.'

  return jsonify({'status': status, 'message': message})


# sTODO: GET /api/wine/recommendation?min_year=<>&max_year=<>
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

# ideas of API calls
# GET /api/wine/<wine_id>
# GET /api/user/<user_id>/wine-recommendations

# option 1: benefits - easy to understand, can be slower with making lots api calls at once
# GET /api/wine/years -> json: {years: [1980, 1970, 1960, ...]}
# GET /api/wine/price -> json: {price: [20, 30, 40, ...]}
# option 2: benefits - faster
# ----> GET /api/wine/data -> json: {years: [1980, ...], price: [20, ...]}


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)





