#!/usr/bin/python3
"""class User is defined here to inherit from BaseModel"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """class User inherits from BaseModel
    Arguments:
        email = empty string
        password = emtpy string
        first_name = empty string
        last_name = empty string
    """

    # public instances
    email = ""
    password = ""
    first_name = ""
    last_name = ""
