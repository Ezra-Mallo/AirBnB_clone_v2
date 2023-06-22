#!/bin/usr/env python3
"""class State defined here to inherit from BaseModel"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """class State inherit from BaseModel
    Arguments:
        name = empty string
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if os.getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            """All cities associated with city id."""
            cities_list = []
            # from models import storage
            # all_object = storage.all()
            # review_list = []
            from models.city import City
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
