#!/usr/bin/python3
"""module documentation"""

from modules.base_model import BaseModel


class Review(BaseModel):
    """a child class of BaseModel has 3 attributes"""

    place_id = ""
    user_id = ""
    text = ""
