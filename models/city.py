#!/usr/bin/python3
"""City Module for HBNB project."""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """class City inherit from BaseModel
    Arguments:
        state_id = string - empty string: it will be the State.id
        name = string - empty string
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60),
                      ForeignKey("states.id", ondelete="CASCADE"),
                      nullable=False)
#    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
#    places = relationship("Place", backref="cities", cascade="all, delete")
