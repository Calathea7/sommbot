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
  print("hitting the rec route \n \n \n")
  print(request.get_json())

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





