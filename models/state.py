#!/usr/bin/python3
<<<<<<< HEAD
"""class State defined here to inherit from BaseModel"""

import models
=======
""" State Module for HBNB project """
>>>>>>> 34c75eecab35b634ff48eaa13531ab0307292ffe
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
import os


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            '''A getter method for cities from file storage'''
            cities = models.storage.all(City).values()
            cities_list = [city for city in cities if self.id == city.state_id]
            return cities_list
