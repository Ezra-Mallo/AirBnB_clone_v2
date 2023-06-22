#!/usr/bin/python3
"""Basemodel class is defined here"""
import models
import datetime
from uuid import uuid4
from sqlalchemy import create_engine, String, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base

db_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}',
                          pool_pre_ping=True)
Base = declarative_base()


class BaseModel:
    """This is basemodel class"""

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False,
                        default=datetime.datetime.now())
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.datetime.now())

    def __init__(self, *args, **kwargs):
        """Initialization of the instance
            Args:
                *args = argument variables
                **kwargs = keyword variables
            Raises:
                none
        """
        my_dict = {}
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        date_value = datetime.datetime.fromisoformat(value)
                        self.__dict__[key] = date_value
                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        This module returns the string represation
        """
        myStr = ("[{}] ({}) {}".format(self.__class__.__name__,
                                       self.id, self.__dict__))
        return myStr

    def save(self):
        """
        This updated the "updated_date" and saves it
        """
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        This returns a dictionary containing all keys/values
        of __dict__ of the instance:
        """
        """
        dict_temp_file = self.__dict__.copy()
        dict_temp_file["created_at"] = self.created_at.isoformat()
        dict_temp_file["updated_at"] = self.updated_at.isoformat()
        dict_temp_file["__class__"] = self.__class__.__name__
        return dict_temp_file"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """This method delete the current instance from the storage
        (models.storage) by calling the method"""
        models.storage.delete(self)
