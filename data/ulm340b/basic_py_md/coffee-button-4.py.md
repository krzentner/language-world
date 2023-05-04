
'''

# Define `coffee_button` below this line

# BEGIN SOLUTION

# coffee-button: push the button on the coffee machine
def coffee_button(robot):
    if check("the robot's gripper is not vertically aligned with coffee button"):
        robot.move("gripper above coffee button")
    if check("the robot's gripper is vertically aligned with coffee button and the robot's gripper is not near coffee button"):
        robot.push("down on coffee button")

# END SOLUTION


[eod] [code]from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float, UniqueConstraint, ForeignKey, DateTime, Date
from database_connection import connect_to_db

Base = declarative_base()


class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    dob = Column(DateTime)


class Person2(Base):
    __tablename__ = "people2"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    dob = Column(DateTime)


class Person3(Base):
    __tablename__ = "people3"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    dob = Column(DateTime)


class Person4(Base):
    __tablename__ = "people4"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    dob = Column(DateTime)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    person_id = Column(Integer, ForeignKey("people.id"))


class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    balance = Column(Integer, default=0)


class Transaction(Base):
    __tablename__ = "transactions"
    account_id = Column(Integer, ForeignKey("accounts