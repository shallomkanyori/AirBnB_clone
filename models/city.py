#!/usr/bin/python3
"""A class that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """a child class of BaseModel with two attributes"""

    state_id = ""
    name = ""
