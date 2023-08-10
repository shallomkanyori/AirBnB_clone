#!/usr/bin/python
"""a class that inherits from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """A child class of baseModel representing state"""
    name = ""
