#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in a database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes DBStorage instance"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.environ['HBNB_MYSQL_USER'],
                                              os.environ['HBNB_MYSQL_PWD'],
                                              os.environ['HBNB_MYSQL_HOST'],
                                              os.environ['HBNB_MYSQL_DB']),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in the database"""
        classes = [User, State, City, Amenity, Place, Review]
        objects = {}
        if cls:
            query = self.__session.query(cls).all()
            for obj in query:
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        else:
            for cls in classes:
                query = self.__session.query(cls).all()
                for obj in query:
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        """Adds new object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and creates session"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
