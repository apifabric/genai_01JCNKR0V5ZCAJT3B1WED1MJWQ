# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime

logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


class User(Base):
    """description: Stores details about users who plan holidays."""
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    signup_date = Column(DateTime, default=datetime.utcnow)


class Holiday(Base):
    """description: Represents holiday plans."""
    __tablename__ = 'holiday'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)


class Activity(Base):
    """description: Represents activities planned in a holiday."""
    __tablename__ = 'activity'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(Date)
    holiday_id = Column(Integer, ForeignKey('holiday.id'), nullable=False)
    review_id = Column(Integer, ForeignKey('review.id'))


class Review(Base):
    """description: Stores reviews for activities."""
    __tablename__ = 'review'
    
    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    comment = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)


class Airport(Base):
    """description: Represents airports managed by the system."""
    __tablename__ = 'airport'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    city = Column(String)
    country = Column(String)


class Flight(Base):
    """description: Represents flights departing or arriving at airports."""
    __tablename__ = 'flight'
    
    id = Column(Integer, primary_key=True)
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)
    source_airport_id = Column(Integer, ForeignKey('airport.id'), nullable=False)
    destination_airport_id = Column(Integer, ForeignKey('airport.id'), nullable=False)


class Booking(Base):
    """description: Represents bookings for flights."""
    __tablename__ = 'booking'
    
    id = Column(Integer, primary_key=True)
    booking_date = Column(DateTime, default=datetime.utcnow)
    flight_id = Column(Integer, ForeignKey('flight.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)


class Passenger(Base):
    """description: Represents passengers on a booked flight."""
    __tablename__ = 'passenger'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    booking_id = Column(Integer, ForeignKey('booking.id'), nullable=False)


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

# Test data for User
user1 = User(name="Alice Wonderland", email="alice@example.com", signup_date=date(2022, 5, 1))
user2 = User(name="Bob Builder", email="bob@example.com", signup_date=date(2021, 6, 10))
user3 = User(name="Charlie Chocolate", email="charlie@example.com", signup_date=date(2021, 8, 15))
user4 = User(name="Daisy Duke", email="daisy@example.com", signup_date=date(2023, 1, 20))

# Test data for Holiday
holiday1 = Holiday(name="Summer Escape", start_date=date(2023, 7, 5), end_date=date(2023, 7, 15), user_id=1)
holiday2 = Holiday(name="Winter Wonderland", start_date=date(2023, 12, 5), end_date=None, user_id=2)
holiday3 = Holiday(name="Spring Fling", start_date=date(2023, 4, 10), end_date=date(2023, 4, 20), user_id=3)
holiday4 = Holiday(name="Autumn Adventure", start_date=date(2023, 10, 1), end_date=None, user_id=4)

# Test data for Activity
activity1 = Activity(name="Beach Volleyball", date=date(2023, 7, 7), holiday_id=1)
activity2 = Activity(name="Mountain Hiking", date=date(2023, 12, 6), holiday_id=2)
activity3 = Activity(name="City Tour", date=date(2023, 4, 12), holiday_id=3)
activity4 = Activity(name="Wine Tasting", date=date(2023, 10, 3), holiday_id=4)

# Test data for Review
review1 = Review(rating=5, comment="Amazing experience!", user_id=1)
review2 = Review(rating=4, comment="Really fun.", user_id=2)
review3 = Review(rating=3, comment="Good but could be better.", user_id=1)
review4 = Review(rating=2, comment="Not as expected.", user_id=3)

# Test data for Airport
airport1 = Airport(name="JFK International", city="New York", country="USA")
airport2 = Airport(name="Heathrow", city="London", country="UK")
airport3 = Airport(name="Changi", city="Singapore", country="Singapore")
airport4 = Airport(name="Dubai International", city="Dubai", country="UAE")

# Test data for Flight
flight1 = Flight(departure_time=datetime(2023, 5, 1, 9, 0), arrival_time=datetime(2023, 5, 1, 12, 30), source_airport_id=1, destination_airport_id=2)
flight2 = Flight(departure_time=datetime(2023, 5, 3, 15, 0), arrival_time=datetime(2023, 5, 3, 19, 0), source_airport_id=2, destination_airport_id=3)
flight3 = Flight(departure_time=datetime(2023, 5, 5, 11, 0), arrival_time=datetime(2023, 5, 5, 15, 30), source_airport_id=3, destination_airport_id=4)
flight4 = Flight(departure_time=datetime(2023, 5, 7, 22, 0), arrival_time=datetime(2023, 5, 8, 2, 0), source_airport_id=4, destination_airport_id=1)

# Test data for Booking
booking1 = Booking(booking_date=datetime(2023, 4, 15), flight_id=1, user_id=1)
booking2 = Booking(booking_date=datetime(2023, 4, 16), flight_id=2, user_id=2)
booking3 = Booking(booking_date=datetime(2023, 4, 17), flight_id=3, user_id=3)
booking4 = Booking(booking_date=datetime(2023, 4, 18), flight_id=4, user_id=4)

# Test data for Passenger
passenger1 = Passenger(name="Elena Gilbert", age=25, booking_id=1)
passenger2 = Passenger(name="Damian Salvatore", age=28, booking_id=2)
passenger3 = Passenger(name="Stefan Salvatore", age=27, booking_id=3)
passenger4 = Passenger(name="Bonnie Bennett", age=26, booking_id=4)



session.add_all([user1, user2, user3, user4, holiday1, holiday2, holiday3, holiday4, activity1, activity2, activity3, activity4, review1, review2, review3, review4, airport1, airport2, airport3, airport4, flight1, flight2, flight3, flight4, booking1, booking2, booking3, booking4, passenger1, passenger2, passenger3, passenger4])
session.commit()
