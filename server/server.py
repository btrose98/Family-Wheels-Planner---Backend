from flask import Flask

from server.routes.car_routes import car_blueprint
from server.routes.people_routes import people_blueprint
from server.routes.reservation_routes import reservation_blueprint
from database.database import check_if_database_exists, create_database
from utils.test_data import insert_database_test_data

app = Flask(__name__)

app.register_blueprint(people_blueprint)
app.register_blueprint(car_blueprint)
app.register_blueprint(reservation_blueprint)

@app.route("/")
def home():
    return "Home of Family-Wheels-Planner---Backend"

def run_app():
    if not check_if_database_exists():
        print("Database does not exist. Creating one now ...")
        create_database()
        insert_database_test_data()

    app.run(host='0.0.0.0', port=5000)