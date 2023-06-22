#!/usr/bin/python3
"""class User is defined here to inherit from BaseModel"""
import models
<<<<<<< HEAD
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


=======
from models.base_model import BaseModel, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

>>>>>>> 4d76ea0b3001ec29f14958b4a277104b7fdfdcfd
class User(BaseModel, Base):
    """class User inherits from BaseModel
    Arguments:
        email = empty string
        password = emtpy string
        first_name = empty string
        last_name = empty string
    """

    # public instances
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
<<<<<<< HEAD
    last_name = Column(String(128), nullable=True)
=======
    last_name =  Column(String(128), nullable=True)
>>>>>>> 4d76ea0b3001ec29f14958b4a277104b7fdfdcfd
