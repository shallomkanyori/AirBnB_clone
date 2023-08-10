#!/usr/bin/python3
"""a class user inheriting from the baseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """A class representation of the user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
