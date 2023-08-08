#!/usr/bin/python3
"""This module defines the BaseModel class."""
from datetime import datetime
import uuid


class BaseModel():
    """The base class for all other models."""

    def __init__(self):
        """Initializes the instance.
            Attributes:
                id (str): the uuid of the instance.
                created_at (datetime): the datetime of the instance's creation.
                updated_at (datetime): the datetime of the instance's updating.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation of an instance."""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute updated_at
            Updates updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns the dictionary representation of the instance."""
        res_dict = self.__dict__.copy()

        res_dict["__class__"] = type(self).__name__

        res_dict["created_at"] = datetime.isoformat(self.created_at)
        res_dict["updated_at"] = datetime.isoformat(self.updated_at)

        return res_dict
