#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from os import getenv
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, scoped_session, sessionmaker


class DBStorage:
    """Define DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance."""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.format(
                getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB"),
                pool_pre_ping=True))

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session all objects of
        the given class."""
        if cls is None:
            objects = self.__session.query(State).all()
            objects.extend(self.__session.query(City).all())
            objects.extend(self.__session.query(User).all())
            objects.extend(self.__session.query(Place).all())
            objects.extend(self.__session.query(Review).all())
            objects.extend(self.__session.query(Amenity).all())
        else:
            objects = self.__session.query(cls).all()
        dico = {
            "{}.{}".format(obj.__class__.__name__, obj.id):
            obj for obj in objects}
        return dico

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session
        (self.__session)"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Close the SQLAlchemy session."""
        self.__session.close()
