#!/usr/bin/env python3
import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import re
import os


def tokenize(args: str) -> list:
    """Tokenizer.
    Args:
        args (str): Description

    Returns:
        list: Description
    """
    pattern = r"^(?P<name>[A-Za-z0-9]+)"
    param_pattern = r"(?P<params>\w+=(\"[^\"]+\"|[\d\.-]+))"

    class_validator = re.compile(pattern)
    params_validator = re.compile(param_pattern)

    obj_class = class_validator.findall(args)
    obj_param = params_validator.findall(args)

    if len(obj_class) != 0:
        token.append(obj_class[0])
    token.append([data[0] for data in obj_param])
    print(token)
    return token


class HBNBCommand(cmd.Cmd):
    """This class is the entry point of the command interpreter."""

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

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to JSON file) and
        prints the id. Ex: $ create BaseModel"""

        print(arg)
        print("------------------------------------\n")
        tokens = tokenize(arg)
        raise SystemExit
        # check if args passed
        if arg == "" or len(tokens) < 2:
            print("** class name missing **")
            return
        # extract the class name
        class_name = tokens[0]
        # extract all params
        params = tokens[1]

        # if class not in class
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        # create a new class instance
        new_instance = HBNBCommand.__classes[class_name]()
        # loop through all params and setattr to the object instance
        for param in params:
            try:
                k, v = param.split("=")
                v = v.replace("_", " ")
                if v[0] == '"' and v[-1] == '"' and len(v) > 1:
                    v = v[1:-1]
                elif "." in v:
                    v = float(v)
                else:
                    v = int(v)
                setattr(new_instance, k, v)
            except ValueError:
                continue
        new_instance.save()
        print(new_instance.id)
        storage.save()
# ------------------------------------------------------------------------------
"""        if len(arg) == 0:
            "" Check if argument was passed""
            print("** class name missing **")
            return False
        else:
            # to split the arg and remove plant spaces
            myArgs = re.split(' ', arg)
            while '' in myArgs:
                myArgs.remove('')

            # convet to dictionary & clean the values up starting from index 1
            if myArgs[0] not in HBNBCommand.__classes:
                "" Check if class name argument was passed""
                print("** class doesn't exist **")
                return False
            elif len(myArgs) == 1:
                new_instance = HBNBCommand.__classes[myArgs[0]]()
                storage.new(new_instance)
                storage.save()
                print(new_instance.id)
                return False
            elif len(myArgs) >= 3:
                new_instance = HBNBCommand.__classes[myArgs[0]]()
                for my_Arg in myArgs[1:]:
                    try:
                        key, val = my_Arg.split("=")
                        val= val.replace("_", " ")
                        if val[0] == '"' and val[-1] == '"' and len(val) > 1:
                            val = val[1:-1]
                        elif "." in val:
                            val = float(val)
                        else:
                            val = int(val)
                        setattr(new_instance, key, val)
                    except ValueError:
                        continue
                raise SystemExit
                storage.save()
                """

    def do_show(self, arg):
        """Prints the string representation of an instance based on the
        class name and id. Ex: $ show BaseModel 1234-1234-1234."""

        if len(arg) == 0:
            """ Check if argument was passed"""
            print("** class name missing **")
        else:
            myArgs = arg.split()
            if myArgs[0] not in HBNBCommand.__classes:
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
        not on the class name. Ex: $ all BaseModel or $ all.
        """
        my_print_list = []
        if arg:
            # This splits arg and assigns index 0 of the split to arg
            arg = arg.split(' ')[0]
            if arg not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return False
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

#    def all(self, line):
#        """    parses the regex and run if it matches.
#        """
#        my_re = r"({})?\.?(all\(\))?".format("|".join(self.model_dict.keys()))
#        regex = re.compile(my_re)
#        model, cond = regex.search(line).groups()
#        if not cond:
#            return False
#        if cond and model in self.model_dict.keys():
#            result = storage.all()
#            for k, v in result.items():
#                if k.split(".")[0] == model:
#                    print(v)
#            return True
#        else:
#            print("** class doesn't exist **")
#            return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
