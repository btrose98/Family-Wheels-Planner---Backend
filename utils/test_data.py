from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Person, Car, Reservation
from pytz import timezone

file_path = "database/reservationdb.db"
engine = create_engine("sqlite:///" + file_path, echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def insert_database_test_data():
    print("Creating test data to insert into database...\n")
    testPerson = Person(firstname="Test", lastname="User")
    session.add(testPerson)
    session.commit()

    testCar = Car(brand="Hyundai", owner=testPerson.id)
    session.add(testCar)
    session.commit()

    tz = timezone("US/Eastern")
    current_time = datetime.now(tz)
    test_startdatetime = current_time
    test_enddatetime = current_time + timedelta(hours=1)
    testReservation = Reservation(startdatetime=test_startdatetime, enddatetime=test_enddatetime, owner=testPerson.id, car=testCar.id)
    session.add(testReservation)
    session.commit()

    results = session.query(Reservation).all()
    print(f"test data:\n{results}")


if __name__ == "__main__":
    insert_database_test_data()