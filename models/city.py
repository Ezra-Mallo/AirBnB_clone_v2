#!/bin/usr/env python3
"""class City defined here to inherit from BaseModel"""

import models
from models.base_model import BaseModel


class City(BaseModel):
    """class City inherit from BaseModel
    Arguments:
        state_id = string - empty string: it will be the State.id
        name = string - empty string
    """
    state_id = ""
    name = ""
