#!/usr/bin/env python3

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    """
    This class is the entry point of the command interpreter."""

    # intro = 'Welcome to hbnb shell.'
    prompt = "(hnbn) "
    __classes = {"BaseModel": BaseModel, "User": User, "State": State,
                 "Place": Place, "City": City, "Amenity": Amenity,
                 "Review": Review}

    def emptyline(self):
        """Does Nothing."""
        pass

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

# ----------------------------------------------------------------------------
    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to JSON file) and
        prints the id. Ex: $ create BaseModel"""
        myArgs = re.split(' |=|"', arg)
        while '' in myArgs:
            myArgs.remove('')

        if len(myArgs) == 0:

            """ Check if argument was passed"""
            print("** class name missing **")
        elif myArgs[0] not in HBNBCommand.__classes:
            """ Check if class name argument was passed"""
            print("** class doesn't exist **")
        elif len(myArgs) == 1:
            new_instance = HBNBCommand.__classes[myArgs[0]]()
            storage.new(new_instance)
            storage.save()
            print(new_instance.id)
        elif len(myArgs) >= 3:
            new_instance = HBNBCommand.__classes[myArgs[0]]()
            storage.new(new_instance)
            storage.save()
            print(new_instance.id)
            class_name = myArgs[0]
            instance_id = new_instance.id

            attributes = {}
            for number in range(1, len(myArgs), 2):
                attributes[myArgs[number]] = myArgs[number + 1]

            instance_Key = "{}.{}".format(class_name, instance_id)
            Class_Instance = storage.all()
            if instance_Key in Class_Instance.keys():
                instance_pointer = Class_Instance[instance_Key]
                for key, value in attributes.items():
                    setattr(instance_pointer, key, value)
                storage.save()

# ----------------------------------------------------------------------------

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id. Ex: $ show BaseModel 1234-1234-1234."""

        myArgs = arg.split()
        if len(myArgs) == 0:
            """ Check if argument was passed"""
            print("** class name missing **")
        elif myArgs[0] not in HBNBCommand.__classes:
            """ Check if class name argument was passed"""
            print("** class doesn't exist ** ")
        elif len(myArgs) < 2:
            print("** instance id missing **")
        else:
            class_name = myArgs[0]
            instance_id = myArgs[1]

            instance_Key = "{}.{}".format(class_name, instance_id)
            class_instance = storage.all()

            if instance_Key in class_instance:
                print(class_instance[instance_Key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.and"""

        myArgs = arg.split()
        if len(myArgs) == 0:
            """ Check if argument was passed"""
            print("** class name missing **")
        elif myArgs[0] not in HBNBCommand.__classes:
            """ Check if class name argument was passed"""
            print("** class doesn't exist ** ")
        elif len(myArgs) < 2:
            """ Check if class instance id argument was passed"""
            print("** instance id missing **")
        else:
            class_name = myArgs[0]
            instance_id = myArgs[1]

            instance_Key = "{}.{}".format(class_name, instance_id)
            class_instance = storage.all()

            """ Search for the instance (class_name.instnace_id) in the
            JSON dictionary"""
            if instance_Key in class_instance:
                del class_instance[instance_Key]

            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or
        not on the class name. Ex: $ all BaseModel or $ all."""
        my_print_list = []
        if arg:
            # This assigned index 0 of the split to arg
            arg = arg.split(' ')
            if arg not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            for key, value in storage.all().items():
                if key.split('.')[0] == arg:
                    my_print_list.append(str(value))
        else:
            for key, value in storage.all().items():
                my_print_list.append(str(value))
        print(my_print_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"""

        myArgs = arg.split()
        if len(myArgs) == 0:
            """ Check if argument was passed"""
            print("** class name missing **")
        elif myArgs[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(myArgs) < 2:
            """ Check if class instance id argument was passed"""
            print("** instance id missing **")
        elif len(myArgs) < 3:
            print("** attribute name missing **")
        elif len(myArgs) < 4:
            print("** value missing **")
        else:
            class_name = myArgs[0]
            instance_id = myArgs[1]
            attr_key = myArgs[2]
            attr_val = myArgs[3]

            instance_Key = "{}.{}".format(class_name, instance_id)
            Class_Instance = storage.all()

            if instance_Key in Class_Instance.keys():
                # to update, use:
                # class_instance[instance_key].__dict__[attr_key] = attr_val
                # or
                instance_pointer = Class_Instance[instance_Key]
                setattr(instance_pointer, attr_key, attr_val)

                # to save, use: class_instance[instance_key].save
                # or
                storage.save()
            else:
                print("** no instance found **")

    def all(self, line):
        """all method up be called by default,
        parses the regex and run if it matches.
        """
        my_re = r"({})?\.?(all\(\))?".format("|".join(self.model_dict.keys()))
        regex = re.compile(my_re)
        model, cond = regex.search(line).groups()
        if not cond:
            return False
        if cond and model in self.model_dict.keys():
            result = storage.all()
            for k, v in result.items():
                if k.split(".")[0] == model:
                    print(v)
            return True
        else:
            print("** class doesn't exist **")
            return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
