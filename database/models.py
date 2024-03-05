import sqlalchemy as sa
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, DateTime
from database.database import Base


class Person(Base):
    __tablename__ = "people"

    id = sa.Column("id", Integer, primary_key=True, autoincrement=True)
    firstname = sa.Column("firstname", String)
    lastname = sa.Column("lastname", String)

    def __repr__(self):
        return f"({self.id}) {self.firstname} {self.lastname}"

class Car(Base):
    __tablename__ = "cars"

    id = sa.Column("id", Integer, primary_key=True, autoincrement=True)
    brand = sa.Column("brand", String)
    owner = sa.Column(Integer, ForeignKey("people.id"))

    def __repr__(self):
        return f"({self.id}) {self.desciption} owned by {self.owner}"

class Reservation(Base):
    __tablename__ = "reservations"

    id = sa.Column("id", Integer, primary_key=True, autoincrement=True)
    startdatetime = sa.Column("startdatetime", DateTime)
    enddatetime = sa.Column("enddatetime", DateTime)
    owner = sa.Column(Integer, ForeignKey("people.id"))
    car = sa.Column(Integer, ForeignKey("cars.id"))

    def __repr__(self):
        return f"({self.id}): {self.owner}, {self.car} @ {self.startdatetime} - {self.enddatetime}"