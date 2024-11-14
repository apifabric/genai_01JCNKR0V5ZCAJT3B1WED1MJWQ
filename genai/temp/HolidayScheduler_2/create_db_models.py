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


class Holiday(Base):
    """description: Represents a holiday plan."""

    __tablename__ = 'holiday'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    destination = Column(String, nullable=False)


class Activity(Base):
    """description: Represents an activity within a holiday."""

    __tablename__ = 'activity'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    holiday_id = Column(Integer, ForeignKey('holiday.id'), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    location = Column(String, nullable=False)


class Review(Base):
    """description: Represents a review for an activity."""

    __tablename__ = 'review'

    id = Column(Integer, primary_key=True, autoincrement=True)
    activity_id = Column(Integer, ForeignKey('activity.id'), nullable=False)
    review_text = Column(Text)
    rating = Column(Integer)
    review_date = Column(Date, nullable=False)


class Airport(Base):
    """description: Represents an airport."""

    __tablename__ = 'airport'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)


class Flight(Base):
    """description: Represents a scheduled flight."""

    __tablename__ = 'flight'

    id = Column(Integer, primary_key=True, autoincrement=True)
    flight_number = Column(String, nullable=False)
    departure_time = Column(DateTime, nullable=False)
    arrival_time = Column(DateTime, nullable=False)
    departure_airport_id = Column(Integer, ForeignKey('airport.id'), nullable=False)
    arrival_airport_id = Column(Integer, ForeignKey('airport.id'), nullable=False)
    total_seats = Column(Integer, nullable=False)


class Booking(Base):
    """description: Represents a flight booking."""

    __tablename__ = 'booking'

    id = Column(Integer, primary_key=True, autoincrement=True)
    flight_id = Column(Integer, ForeignKey('flight.id'), nullable=False)
    passenger_id = Column(Integer, ForeignKey('passenger.id'), nullable=False)
    seat_number = Column(String, nullable=False)
    booking_date = Column(Date, nullable=False)


class Passenger(Base):
    """description: Represents a flight passenger."""

    __tablename__ = 'passenger'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    passport_number = Column(String, nullable=False)
    nationality = Column(String, nullable=False)


class HolidayActivityLink(Base):
    """description: Represents a link between holidays and activities."""

    __tablename__ = 'holiday_activity_link'

    id = Column(Integer, primary_key=True, autoincrement=True)
    holiday_id = Column(Integer, ForeignKey('holiday.id'), nullable=False)
    activity_id = Column(Integer, ForeignKey('activity.id'), nullable=False)


class FlightBookingLink(Base):
    """description: Intersects flights and bookings."""

    __tablename__ = 'flight_booking_link'

    id = Column(Integer, primary_key=True, autoincrement=True)
    flight_id = Column(Integer, ForeignKey('flight.id'), nullable=False)
    booking_id = Column(Integer, ForeignKey('booking.id'), nullable=False)


class AirportFlightLink(Base):
    """description: Intersects airports and flights."""

    __tablename__ = 'airport_flight_link'

    id = Column(Integer, primary_key=True, autoincrement=True)
    airport_id = Column(Integer, ForeignKey('airport.id'), nullable=False)
    flight_id = Column(Integer, ForeignKey('flight.id'), nullable=False)


class FlightPassengerLink(Base):
    """description: Intersects flights and passengers."""

    __tablename__ = 'flight_passenger_link'

    id = Column(Integer, primary_key=True, autoincrement=True)
    flight_id = Column(Integer, ForeignKey('flight.id'), nullable=False)
    passenger_id = Column(Integer, ForeignKey('passenger.id'), nullable=False)


class ActivityReviewLink(Base):
    """description: Intersects activities and reviews."""

    __tablename__ = 'activity_review_link'

    id = Column(Integer, primary_key=True, autoincrement=True)
    activity_id = Column(Integer, ForeignKey('activity.id'), nullable=False)
    review_id = Column(Integer, ForeignKey('review.id'), nullable=False)


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

# Holiday Test Data
holiday1 = Holiday(name="Summer Getaway", start_date=date(2023, 6, 1), end_date=date(2023, 6, 15), destination="Hawaii")
holiday2 = Holiday(name="Winter Wonderland", start_date=date(2023, 12, 1), end_date=date(2023, 12, 10), destination="Switzerland")
holiday3 = Holiday(name="Autumn Retreat", start_date=date(2023, 9, 20), end_date=date(2023, 9, 25), destination="Japan")
holiday4 = Holiday(name="Spring Escape", start_date=date(2023, 3, 10), end_date=date(2023, 3, 20), destination="Australia")

# Activity Test Data
activity1 = Activity(name="Surfing Lesson", holiday_id=holiday1.id, start_time=datetime(2023, 6, 3, 9, 0), end_time=datetime(2023, 6, 3, 11, 0), location="Waikiki Beach")
activity2 = Activity(name="Snowboarding", holiday_id=holiday2.id, start_time=datetime(2023, 12, 2, 10, 0), end_time=datetime(2023, 12, 2, 13, 0), location="Alps")
activity3 = Activity(name="Cherry Blossom Viewing", holiday_id=holiday3.id, start_time=datetime(2023, 9, 21, 15, 0), end_time=datetime(2023, 9, 21, 17, 0), location="Tokyo")
activity4 = Activity(name="Great Barrier Reef Diving", holiday_id=holiday4.id, start_time=datetime(2023, 3, 12, 9, 0), end_time=datetime(2023, 3, 12, 12, 0), location="Queensland")

# Review Test Data
review1 = Review(activity_id=activity1.id, review_text="Amazing experience!", rating=5, review_date=date(2023, 6, 4))
review2 = Review(activity_id=activity2.id, review_text="Breathtaking views.", rating=4, review_date=date(2023, 12, 3))
review3 = Review(activity_id=activity3.id, review_text="Beautiful scenery.", rating=5, review_date=date(2023, 9, 22))
review4 = Review(activity_id=activity4.id, review_text="Spectacular dive.", rating=5, review_date=date(2023, 3, 13))

# Airport Test Data
airport1 = Airport(code="HNL", name="Daniel K. Inouye International Airport", location="Honolulu, HI")
airport2 = Airport(code="ZRH", name="Zurich Airport", location="Zurich, Switzerland")
airport3 = Airport(code="NRT", name="Narita International Airport", location="Tokyo, Japan")
airport4 = Airport(code="SYD", name="Sydney Airport", location="Sydney, Australia")

# Flight Test Data
flight1 = Flight(flight_number="HA123", departure_time=datetime(2023, 6, 1, 14, 0), arrival_time=datetime(2023, 6, 1, 20, 0), departure_airport_id=airport1.id, arrival_airport_id=airport2.id, total_seats=250)
flight2 = Flight(flight_number="SW321", departure_time=datetime(2023, 12, 1, 16, 0), arrival_time=datetime(2023, 12, 1, 20, 0), departure_airport_id=airport2.id, arrival_airport_id=airport3.id, total_seats=200)
flight3 = Flight(flight_number="JL200", departure_time=datetime(2023, 9, 20, 10, 0), arrival_time=datetime(2023, 9, 20, 16, 0), departure_airport_id=airport3.id, arrival_airport_id=airport4.id, total_seats=180)
flight4 = Flight(flight_number="QF400", departure_time=datetime(2023, 3, 10, 12, 0), arrival_time=datetime(2023, 3, 10, 18, 0), departure_airport_id=airport4.id, arrival_airport_id=airport1.id, total_seats=220)

# Booking Test Data
booking1 = Booking(flight_id=flight1.id, passenger_id=1, seat_number="12A", booking_date=date(2023, 5, 1))
booking2 = Booking(flight_id=flight2.id, passenger_id=2, seat_number="8B", booking_date=date(2023, 11, 2))
booking3 = Booking(flight_id=flight3.id, passenger_id=3, seat_number="20C", booking_date=date(2023, 8, 15))
booking4 = Booking(flight_id=flight4.id, passenger_id=4, seat_number="15D", booking_date=date(2023, 2, 25))

# Passenger Test Data
passenger1 = Passenger(name="John Doe", date_of_birth=date(1980, 1, 1), passport_number="A1234567", nationality="USA")
passenger2 = Passenger(name="Jane Smith", date_of_birth=date(1990, 2, 15), passport_number="B7654321", nationality="Canada")
passenger3 = Passenger(name="Emma Johnson", date_of_birth=date(1985, 5, 23), passport_number="C8765432", nationality="UK")
passenger4 = Passenger(name="Liam Brown", date_of_birth=date(1995, 3, 30), passport_number="D1239876", nationality="Australia")


session.add_all([holiday1, holiday2, holiday3, holiday4, activity1, activity2, activity3, activity4, review1, review2, review3, review4, airport1, airport2, airport3, airport4, flight1, flight2, flight3, flight4, booking1, booking2, booking3, booking4, passenger1, passenger2, passenger3, passenger4])
session.commit()
