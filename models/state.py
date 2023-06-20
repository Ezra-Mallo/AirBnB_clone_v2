#!/bin/usr/env python3
"""class State defined here to inherit from BaseModel"""

import models
from models.base_model import BaseModel


class State(BaseModel):
    """class State inherit from BaseModel
    Arguments:
        name = empty string
    """

    name = ""
