#!/usr/bin/python3
"""class Review is defined here to inherit from BaseModel"""
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review inherits from BaseModel
    Arguments:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """

    # public instances
    place_id = ""
    user_id = ""
    text = ""
