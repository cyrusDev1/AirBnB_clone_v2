#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from os import getenv
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity


place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey(
        'places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey(
        'amenities.id'), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place", cascade="delete")
    else:
        @property
        def reviews(self):
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return(review)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False)
    else:
        @property
        def amenities(self):
            list_amenity = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    list_amenity.append(amenity)
            return list_amenity

        @amenities.setter
        def amenities(self, obj):
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
