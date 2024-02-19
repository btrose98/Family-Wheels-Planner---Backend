# main.py
from datetime import datetime
from database.models import Person, Car, Reservation
from database.database import Base, Session

if __name__ == '__main__':
    Base.metadata.create_all(bind=Session().get_bind())
    session = Session()

    testPerson = Person(0, "Test", "User")
    session.add(testPerson)

    testCar = Car(0, "Hyundai", testPerson.id)
    session.add(testCar)

    test_startdatetime = datetime(2024, 2, 20, 14, 30)  # February 20, 2024, 2:30 PM
    test_enddatetime = datetime(2024, 2, 20, 15, 45)  # February 20, 2024, 2:30 PM
    testReservation = Reservation(0, test_startdatetime, test_enddatetime, testPerson.id, testCar.id)
    session.add(testReservation)

    session.commit()

    results = session.query(Reservation).all()
    print(results)