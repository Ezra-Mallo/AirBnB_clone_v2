#!/usr/bin/python3
"""Basemodel class is defined here"""

from uuid import uuid4
import datetime
import models


class BaseModel:
    """This is basemodel class"""
    # id = str(uuid4())
    # # created_at = datetime.datetime.now()
    # # updated_at = datetime.datetime.now()

    def __init__(self, *args, **kwargs):
        """Initialization of the instance
            Args:
                *args = argument variables
                **kwargs = keyword variables
            Raises:
                none
        """
        my_dict = {}
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        date_value = datetime.datetime.fromisoformat(value)
                        self.__dict__[key] = date_value
                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        This module returns the string represation
        """
        myStr = ("[{}] ({}) {}".format(self.__class__.__name__,
                                       self.id, self.__dict__))
        return myStr

    def save(self):
        """
        This updated the "updated_date" and saves it
        """
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        This returns a dictionary containing all keys/values
        of __dict__ of the instance:
        """
        dict_temp_file = self.__dict__.copy()
        dict_temp_file["created_at"] = self.created_at.isoformat()
        dict_temp_file["updated_at"] = self.updated_at.isoformat()
        dict_temp_file["__class__"] = self.__class__.__name__
        return dict_temp_file


if __name__ == "__main__":
    # I added this so that I will not have to make the calls from
    # test_base_model_dict.py
    # or
    # test_base_model.py

    # #!/usr/bin/python3
    # from models.base_model import BaseModel

    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89

    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("-1-")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")

    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]),
                                       my_model_json[key]))

    print("-2-")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
