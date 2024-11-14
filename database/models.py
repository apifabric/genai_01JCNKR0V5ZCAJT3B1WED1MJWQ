# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 14, 2024 15:14:20
# Database: sqlite:////tmp/tmp.OUfHzszvYD-01JCNKR0V5ZCAJT3B1WED1MJWQ/HolidayScheduler/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Airport(SAFRSBaseX, Base):
    """
    description: Represents airports managed by the system.
    """
    __tablename__ = 'airport'
    _s_collection_name = 'Airport'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    city = Column(String)
    country = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    FlightList : Mapped[List["Flight"]] = relationship(foreign_keys='[Flight.destination_airport_id]', back_populates="destination_airport")
    sourceFlightList : Mapped[List["Flight"]] = relationship(foreign_keys='[Flight.source_airport_id]', back_populates="source_airport")



class User(SAFRSBaseX, Base):
    """
    description: Stores details about users who plan holidays.
    """
    __tablename__ = 'user'
    _s_collection_name = 'User'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    signup_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    HolidayList : Mapped[List["Holiday"]] = relationship(back_populates="user")
    ReviewList : Mapped[List["Review"]] = relationship(back_populates="user")
    BookingList : Mapped[List["Booking"]] = relationship(back_populates="user")



class Flight(SAFRSBaseX, Base):
    """
    description: Represents flights departing or arriving at airports.
    """
    __tablename__ = 'flight'
    _s_collection_name = 'Flight'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)
    source_airport_id = Column(ForeignKey('airport.id'), nullable=False)
    destination_airport_id = Column(ForeignKey('airport.id'), nullable=False)

    # parent relationships (access parent)
    destination_airport : Mapped["Airport"] = relationship(foreign_keys='[Flight.destination_airport_id]', back_populates=("FlightList"))
    source_airport : Mapped["Airport"] = relationship(foreign_keys='[Flight.source_airport_id]', back_populates=("sourceFlightList"))

    # child relationships (access children)
    BookingList : Mapped[List["Booking"]] = relationship(back_populates="flight")



class Holiday(SAFRSBaseX, Base):
    """
    description: Represents holiday plans.
    """
    __tablename__ = 'holiday'
    _s_collection_name = 'Holiday'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    user_id = Column(ForeignKey('user.id'), nullable=False)

    # parent relationships (access parent)
    user : Mapped["User"] = relationship(back_populates=("HolidayList"))

    # child relationships (access children)
    ActivityList : Mapped[List["Activity"]] = relationship(back_populates="holiday")



class Review(SAFRSBaseX, Base):
    """
    description: Stores reviews for activities.
    """
    __tablename__ = 'review'
    _s_collection_name = 'Review'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    comment = Column(String)
    user_id = Column(ForeignKey('user.id'), nullable=False)

    # parent relationships (access parent)
    user : Mapped["User"] = relationship(back_populates=("ReviewList"))

    # child relationships (access children)
    ActivityList : Mapped[List["Activity"]] = relationship(back_populates="review")



class Activity(SAFRSBaseX, Base):
    """
    description: Represents activities planned in a holiday.
    """
    __tablename__ = 'activity'
    _s_collection_name = 'Activity'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(Date)
    holiday_id = Column(ForeignKey('holiday.id'), nullable=False)
    review_id = Column(ForeignKey('review.id'))

    # parent relationships (access parent)
    holiday : Mapped["Holiday"] = relationship(back_populates=("ActivityList"))
    review : Mapped["Review"] = relationship(back_populates=("ActivityList"))

    # child relationships (access children)



class Booking(SAFRSBaseX, Base):
    """
    description: Represents bookings for flights.
    """
    __tablename__ = 'booking'
    _s_collection_name = 'Booking'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    booking_date = Column(DateTime)
    flight_id = Column(ForeignKey('flight.id'), nullable=False)
    user_id = Column(ForeignKey('user.id'), nullable=False)

    # parent relationships (access parent)
    flight : Mapped["Flight"] = relationship(back_populates=("BookingList"))
    user : Mapped["User"] = relationship(back_populates=("BookingList"))

    # child relationships (access children)
    PassengerList : Mapped[List["Passenger"]] = relationship(back_populates="booking")



class Passenger(SAFRSBaseX, Base):
    """
    description: Represents passengers on a booked flight.
    """
    __tablename__ = 'passenger'
    _s_collection_name = 'Passenger'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    booking_id = Column(ForeignKey('booking.id'), nullable=False)

    # parent relationships (access parent)
    booking : Mapped["Booking"] = relationship(back_populates=("PassengerList"))

    # child relationships (access children)
