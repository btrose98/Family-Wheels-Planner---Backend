from flask import Flask, jsonify, request
from database.database import session
from database.models import Person, Car, Reservation
from server.routes.car_routes import car_blueprint
from server.routes.people_routes import people_blueprint
from server.routes.reservation_routes import reservation_blueprint
from utils.HttpStatus import HttpStatus

app = Flask(__name__)

app.register_blueprint(people_blueprint)
app.register_blueprint(car_blueprint)
app.register_blueprint(reservation_blueprint)

### EXAMPLES ###

@app.route("/")
def home():
    return "Home of Family-Wheels-Planner---Backend"

# @app.route("/get-user/<user_id>")
# def get_user(user_id):
#     return

def run_app():
    app.run(debug=True)