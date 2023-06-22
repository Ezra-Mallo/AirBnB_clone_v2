#!/bin/usr/env python3
"""class City defined here to inherit from BaseModel"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """class City inherit from BaseModel
    Arguments:
        state_id = string - empty string: it will be the State.id
        name = string - empty string
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
#    state_id = Column(String(60), ForeignKey("states.id" ondelete="CASCADE"),
#                      nullable=False)
#   places = relationship("Place", backref="cities", cascade="all, delete")
