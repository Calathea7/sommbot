from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "%?%"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def Homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route("/recommendation", methods=["POST"])
def add_order():

  year = request.form.get("year")
  min_price = request.form.get("min-price", 0)
  max_price = request.form.get("max-price", 3300)
  descriptors = request.form.getlist("descriptor")
  # wines = crud.get_wines_by_filters(year, min_price, max_price...)

  print(descriptors)
  return jsonify({"status": "This route works"})

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)












if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
