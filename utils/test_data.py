from datetime import datetime, timedelta

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models import Person, Car, Reservation

file_path = "database/reservationdb.db"
engine = create_engine("sqlite:///" + file_path, echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def insert_database_test_data():
    print("Creating test data to insert into database...\n")
    testPerson = Person(0, "Test", "User")
    session.add(testPerson)

    testCar = Car(0, "Hyundai", testPerson.id)
    session.add(testCar)

    current_time = datetime.now()
    test_startdatetime = current_time
    test_enddatetime = current_time + timedelta(hours=1)
    testReservation = Reservation(0, test_startdatetime, test_enddatetime, testPerson.id, testCar.id)
    session.add(testReservation)

    session.commit()

    results = session.query(Reservation).all()
    print(f"test data:\n{results}")


if __name__ == "__main__":
    insert_database_test_data()