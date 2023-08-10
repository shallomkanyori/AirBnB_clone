#!/usr/bin/python3
"""defines the file storage"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
    serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary of all objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        class_name = obj.__class__.__name__
        self.__objects[f"{class_name}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file"""

        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects"""

        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)

                for key, value in obj_dict.items():
                    class_name = value.get('__class__')
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass
