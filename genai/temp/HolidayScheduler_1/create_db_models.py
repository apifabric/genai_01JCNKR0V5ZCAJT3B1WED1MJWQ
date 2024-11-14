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


class Destination(Base):
    """description: Represents a travel destination."""
    __tablename__ = 'destination'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    description = Column(Text)


class Activity(Base):
    """description: Represents an activity available at a destination."""
    __tablename__ = 'activity'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    destination_id = Column(Integer, ForeignKey('destination.id'))
    price = Column(Integer)


class Review(Base):
    """description: Represents a review for an activity."""
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text)
    rating = Column(Integer)
    activity_id = Column(Integer, ForeignKey('activity.id'))
    date = Column(DateTime)


class Airport(Base):
    """description: Represents an airport entity."""
    __tablename__ = 'airport'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)


class Flight(Base):
    """description: Represents a flight between airports."""
    __tablename__ = 'flight'

    id = Column(Integer, primary_key=True, autoincrement=True)
    flight_number = Column(String, nullable=False)
    origin_id = Column(Integer, ForeignKey('airport.id'), nullable=False)
    destination_id = Column(Integer, ForeignKey('airport.id'), nullable=False)
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)


class Booking(Base):
    """description: Represents a flight booking made by a passenger."""
    __tablename__ = 'booking'

    id = Column(Integer, primary_key=True, autoincrement=True)
    passenger_id = Column(Integer, ForeignKey('passenger.id'), nullable=False)
    flight_id = Column(Integer, ForeignKey('flight.id'), nullable=False)
    booking_date = Column(DateTime)


class Passenger(Base):
    """description: Represents a passenger who uses the flight services."""
    __tablename__ = 'passenger'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)


class Customer(Base):
    """description: Represents a customer involved in planning holidays."""
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String)


class HolidayPackage(Base):
    """description: Represents a holiday package purchased by a customer."""
    __tablename__ = 'holiday_package'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    destination_id = Column(Integer, ForeignKey('destination.id'), nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)


class PassengerFlightLink(Base):
    """description: Represents a junction table linking passengers and flights."""
    __tablename__ = 'passenger_flight_link'

    id = Column(Integer, primary_key=True, autoincrement=True)
    passenger_id = Column(Integer, ForeignKey('passenger.id'), nullable=False)
    flight_id = Column(Integer, ForeignKey('flight.id'), nullable=False)


class ActivityBooking(Base):
    """description: Represents a booking of a particular activity by a customer during a holiday package."""
    __tablename__ = 'activity_booking'

    id = Column(Integer, primary_key=True, autoincrement=True)
    holiday_package_id = Column(Integer, ForeignKey('holiday_package.id'), nullable=False)
    activity_id = Column(Integer, ForeignKey('activity.id'), nullable=False)
    booking_date = Column(DateTime)


class AirportManager(Base):
    """description: Represents management data for each airport."""
    __tablename__ = 'airport_manager'

    id = Column(Integer, primary_key=True, autoincrement=True)
    airport_id = Column(Integer, ForeignKey('airport.id'), nullable=False)
    manager_name = Column(String, nullable=False)
    contact_number = Column(String)
    email = Column(String)


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

# Destinations Test Data

from datetime import date, datetime

# TestData for Destination
destination_1 = Destination(id=1, name="Paris", country="France", description="An iconic destination.")
destination_2 = Destination(id=2, name="New York", country="USA", description="The city that never sleeps.")
destination_3 = Destination(id=3, name="Tokyo", country="Japan", description="A bustling metropolis.")
destination_4 = Destination(id=4, name="Sydney", country="Australia", description="The harbor city.")

# TestData for Activity
activity_1 = Activity(id=1, name="Eiffel Tower Visit", description="Visit the iconic Eiffel Tower.", destination_id=1, price=50)
activity_2 = Activity(id=2, name="Statue of Liberty Tour", description="Tour the Statue of Liberty.", destination_id=2, price=40)
activity_3 = Activity(id=3, name="Shinjuku Nightlife Tour", description="Explore Shinjuku's nightlife.", destination_id=3, price=70)
activity_4 = Activity(id=4, name="Sydney Opera House Tour", description="Tour the Sydney Opera House.", destination_id=4, price=60)

# TestData for Review
review_1 = Review(id=1, content="Amazing experience!",


session.add_all([destination_1, destination_2, destination_3, destination_4, activity_1, activity_2, activity_3, activity_4, review_1])
session.commit()
