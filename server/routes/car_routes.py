from flask import Blueprint, jsonify, request
from database.database import session
from database.models import Car
from utils.HttpStatus import HttpStatus

car_blueprint = Blueprint('cars', __name__)

@car_blueprint.route('/cars', methods=['GET'])
def get_cars():
    cars = session.query(Car).all()
    cars_data = [{'id': car.id, 'brand': car.brand, 'owner': car.owner} for car in cars]
    return jsonify(cars_data), HttpStatus.OK

@car_blueprint.route('/cars/<int:id>', methods=['GET'])
def get_car(id):
    car = session.query(Car).get(id)
    if car:
        car_data = {'id': car.id, 'brand': car.brand, 'owner': car.owner}
        return jsonify(car_data), HttpStatus.OK
    else:
        return jsonify({'error': 'Car not found'}), HttpStatus.NOT_FOUND

@car_blueprint.route('/cars', methods=['POST'])
def create_car():
    data = request.get_json()
    new_car = Car(brand=data['brand'], owner=data['owner'])
    session.add(new_car)
    session.commit()
    return jsonify({'id': new_car.id, 'brand': new_car.brand, 'owner': new_car.owner}), HttpStatus.CREATED

@car_blueprint.route('/cars/<int:id>', methods=['PUT'])
def update_car(id):
    data = request.get_json()
    car = session.query(Car).get(id)
    if car:
        car.brand = data.get('brand', car.brand)
        car.owner = data.get('owner', car.owner)
        session.commit()
        return jsonify({'id': car.id, 'brand': car.brand, 'owner': car.owner}), HttpStatus.OK
    else:
        return jsonify({'error': 'Car not found'}), HttpStatus.NOT_FOUND

@car_blueprint.route('/cars/<int:id>', methods=['DELETE'])
def delete_car(id):
    car = session.query(Car).get(id)
    if car:
        session.delete(car)
        session.commit()
        return '', HttpStatus.NO_CONTENT
    else:
        return jsonify({'error': 'Car not found'}), HttpStatus.NOT_FOUND
