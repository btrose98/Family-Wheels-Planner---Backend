from flask import Blueprint, jsonify, request
from database.database import session
from database.models import Person
from utils.http_status import HttpStatus

people_blueprint = Blueprint('people', __name__)

@people_blueprint.route("/people", methods=['GET'])
def get_people():
    people = session.query(Person).all()
    people_data = [{'id': person.id, 'firstname': person.firstname, 'lastname': person.lastname} for person in people]
    return jsonify(people_data), HttpStatus.OK

@people_blueprint.route('/people/<int:id>', methods=['GET'])
def get_person(id):
    person = session.query(Person).get(id)
    if person:
        person_data = {'id': person.id, 'firstname': person.firstname, 'lastname': person.lastname}
        return jsonify(person_data), HttpStatus.OK
    else:
        return jsonify({'error': 'Person not found'}), HttpStatus.NOT_FOUND

@people_blueprint.route('/people', methods=['POST'])
def create_person():
    data = request.get_json()
    new_person = Person(firstname=data['firstname'], lastname=data['lastname'])
    session.add(new_person)
    session.commit()
    return jsonify({'id': new_person.id, 'firstname': new_person.firstname, 'lastname': new_person.lastname}), HttpStatus.CREATED

@people_blueprint.route('/people/<int:id>', methods=['PUT'])
def update_person(id):
    data = request.get_json()
    person = session.query(Person).get(id)
    if person:
        person.firstname = data.get('firstname', person.firstname)
        person.lastname = data.get('lastname', person.lastname)
        session.commit()
        return jsonify({'id': person.id, 'firstname': person.firstname, 'lastname': person.lastname}), HttpStatus.OK
    else:
        return jsonify({'error': 'Person not found'}), HttpStatus.NOT_FOUND

@people_blueprint.route('/people/<int:id>', methods=['DELETE'])
def delete_person(id):
    person = session.query(Person).get(id)
    if person:
        session.delete(person)
        session.commit()
        return '', HttpStatus.NO_CONTENT
    else:
        return jsonify({'error': 'Person not found'}), HttpStatus.NOT_FOUND
