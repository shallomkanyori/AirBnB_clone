#!/usr/bin/python3
"""class inheriting from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """A child class of BaseModel with one attribute"""

    name = ""
