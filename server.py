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


@app.route("/api/recommendation", methods=["POST"])
def recommendation():

  min_year = request.form.get("min-year", 1000)
  max_year = request.form.get("max-year", 2017)
  min_price = request.form.get("min-price", 0)
  max_price = request.form.get("max-price", 3300)
  descriptors = request.form.getlist("descriptor")

  wines = crud.get_wine_by_filters(min_year, max_year, min_price, max_price, descriptors)

  results = [wine[0] for wine in wines]

  return jsonify(results)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)





