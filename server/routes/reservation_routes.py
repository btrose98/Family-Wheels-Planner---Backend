from datetime import datetime
from flask import Blueprint, jsonify, request
from database.database import session
from database.models import Reservation
from utils.HttpStatus import HttpStatus

reservation_blueprint = Blueprint('reservations', __name__)

@reservation_blueprint.route('/reservations', methods=['GET'])
def get_reservations():
    print("get_reservations request")
    current_time = datetime.now()
    reservations = session.query(Reservation).filter(Reservation.enddatetime >= current_time).all()
    reservations_data = [{'id': reservation.id, 'startdatetime': reservation.startdatetime, 'enddatetime': reservation.enddatetime, 'owner': reservation.owner, 'car': reservation.car} for reservation in reservations]
    return jsonify(reservations_data), HttpStatus.OK

@reservation_blueprint.route('/reservations-all', methods=['GET'])
def get_all_reservations():
    reservations = session.query(Reservation).all()
    reservations_data = [{'id': reservation.id, 'startdatetime': reservation.startdatetime, 'enddatetime': reservation.enddatetime, 'owner': reservation.owner, 'car': reservation.car} for reservation in reservations]
    return jsonify(reservations_data), HttpStatus.OK

@reservation_blueprint.route('/reservations/<int:id>', methods=['GET'])
def get_reservation(id):
    reservation = session.query(Reservation).get(id)
    if reservation:
        reservation_data = {'id': reservation.id, 'startdatetime': reservation.startdatetime, 'enddatetime': reservation.enddatetime, 'owner': reservation.owner, 'car': reservation.car}
        return jsonify(reservation_data), HttpStatus.OK
    else:
        return jsonify({'error': 'Reservation not found'}), HttpStatus.NOT_FOUND

@reservation_blueprint.route('/reservations', methods=['POST'])
def create_reservation():
    data = request.get_json()
    new_reservation = Reservation(startdatetime=data['startdatetime'], enddatetime=data['enddatetime'], owner=data['owner'], car=data['car'])
    session.add(new_reservation)
    session.commit()
    return jsonify({'id': new_reservation.id, 'startdatetime': new_reservation.startdatetime, 'enddatetime': new_reservation.enddatetime, 'owner': new_reservation.owner, 'car': new_reservation.car}), HttpStatus.CREATED

@reservation_blueprint.route('/reservations/<int:id>', methods=['PUT'])
def update_reservation(id):
    data = request.get_json()
    reservation = session.query(Reservation).get(id)
    if reservation:
        reservation.startdatetime = data.get('startdatetime', reservation.startdatetime)
        reservation.enddatetime = data.get('enddatetime', reservation.enddatetime)
        reservation.owner = data.get('owner', reservation.owner)
        reservation.car = data.get('car', reservation.car)
        session.commit()
        return jsonify({'id': reservation.id, 'startdatetime': reservation.startdatetime, 'enddatetime': reservation.enddatetime, 'owner': reservation.owner, 'car': reservation.car}), HttpStatus.OK
    else:
        return jsonify({'error': 'Reservation not found'}), HttpStatus.NOT_FOUND

@reservation_blueprint.route('/reservations/<int:id>', methods=['DELETE'])
def delete_reservation(id):
    reservation = session.query(Reservation).get(id)
    if reservation:
        session.delete(reservation)
        session.commit()
        return '', HttpStatus.NO_CONTENT
    else:
        return jsonify({'error': 'Reservation not found'}), HttpStatus.NOT_FOUND
