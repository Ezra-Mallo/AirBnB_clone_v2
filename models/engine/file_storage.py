#!/usr/bin/python3

import json

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Defines FileStorage class

    Attributes:
        __file_path = string, private, file name
        __objects = Dictionary, empty but will grow with value
        __classes
    """
    __file_path = "file.json"
    __objects = {}
    __classes = {"BaseModel": BaseModel, "User": User, "State": State,
                 "Place": Place, "City": City, "Amenity": Amenity,
                 "Review": Review}

    def __init__(self):
        """Initialization"""
        pass

    def all(self, cls=None):
        """
        returns the dictionary __objects
        """
        # return (FileStorage.__objects)
        return (self.__objects)

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        my_key = ("{}.{}".format(obj.__class__.__name__, obj.id))
        # FileStorage.__objects[my_key] = obj
        self.__objects[my_key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        my_temp_dict = {}
        for key, value in FileStorage.__objects.items():
            my_temp_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as myFile:
            json.dump(my_temp_dict, myFile)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""
        try:
            my_reload_dict = {}
            with open(FileStorage.__file_path, "r") as myFil:
                my_reload_dict = json.load(myFil)
                for key, val in my_reload_dict.items():
                    self.all()[key] = self.__classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        This method delete obj from __objects if it exist.
        or does nothing if obj = None
        """
        if obj is not None:
            instance_Key = ("{}.{}".format(obj.__class__.__name__, obj.id))
            class_instance = self.__objects
            if instance_Key in class_instance:
                del class_instance[instance_Key]

    @classmethod
    def set_path(cls, file_path: str):
        """To change the save file path."""
        cls.__file_path = file_path

    @classmethod
    def new_object(cls):
        """Object storage."""
        cls.__objects = {}

    def close(self):
        """Deserialize json file file to objects."""
        self.reload()
