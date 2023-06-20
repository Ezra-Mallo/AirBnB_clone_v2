#!/bin/usr/env python3
"""class Amenity is defined here to inherit from BaseModel"""

import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity inherit from BaseModel
    Arguments:
        name = empty string
    """

    name = ""
