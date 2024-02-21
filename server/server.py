from flask import Flask

from server.routes.car_routes import car_blueprint
from server.routes.people_routes import people_blueprint
from server.routes.reservation_routes import reservation_blueprint

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
    app.run(host='0.0.0.0', port=5000)