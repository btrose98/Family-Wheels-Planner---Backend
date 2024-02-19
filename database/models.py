from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, DateTime
from database.database import Base


class Person(Base):
    __tablename__ = "people"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)

    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return f"({self.id}) {self.firstname} {self.lastname}"

class Car(Base):
    __tablename__ = "cars"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    brand = Column("brand", String)
    owner = Column(Integer, ForeignKey("people.id"))

    def __init__(self, id, brand, owner):
        self.id = id
        self.brand = brand
        self.owner = owner

    def __repr__(self):
        return f"({self.id}) {self.desciption} owned by {self.owner}"

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    startdatetime = Column("startdatetime", DateTime)
    enddatetime = Column("enddatetime", DateTime)
    owner = Column(Integer, ForeignKey("people.id"))
    car = Column(Integer, ForeignKey("cars.id"))

    def __init__(self, id, startdatetime, enddatetime, owner, car):
        self.id = id
        self.startdatetime = startdatetime
        self.enddatetime = enddatetime
        self.owner = owner
        self.car = car

    def __repr__(self):
        return f"({self.id}): {self.owner}, {self.car} @ {self.startdatetime} - {self.enddatetime}"