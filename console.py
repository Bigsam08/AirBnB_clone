#!/usr/bin/python3
"""
Building the HBNB console
program Main Entry
"""
import json
import cmd
import re
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
        class created for our commandline 
        using cmd
    """
    prompt = "(hbnb) "
    classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """ exit the program when user 
            enters quit command
        """
        return True

    def do_EOF(self, arg):
        """ or CTRL + C , EOF signal to exit the program."""
        print("")
        return True

    def emptyline(self):
        """ empty line + ENTER should execute nothing"""
        pass

    def create(self, arg):
        """ creates a new class for each of the following"""
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def show(self, arg):
        """
        shows str rep of instance
        , showing class and id and also err msgs
        """
        arg = arg.split()
        obj_dict = models.storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif f"{arg[0]}.{arg[1]}" not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(argl[0], argl[1])])

    def destroy(self, arg):
        """
        Delete a class instance of a given id
        """
        arg = arg.split()
        obj_dict = models.storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif f"{arg[0]}.{arg[1]}" not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict[F"{arg[0]}.{arg[1]}"]
            storage.save()

    def all(self, arg):
        """
            display all string rep instsnce of all classes
            If no class is specified, displays all instantiated objects.
        """
        arg = arg.split()
        new_list = []
        if len(arg) > 0 and arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if len(arg) > 0 and arg[0] == obj.__class__.__name__:
                    new_list.append(obj.__str__())
                elif len(arg) == 0:
                    new_list.append(obj.__str__())
            print(new_list)

    def update(self, arg):
        """
        Update an instance
        Using class name and id to access attributes for change
        """
        obj_dict = models.storage.all()
        arg = arg.split(" ")

        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
        else:
            key_find = arg[0] + '.' + arg[1]
            obj = obj_dict.get(key_find, None)

            if not obj:
                print("** no instance found **")
                return

            setattr(obj, arg[2], arg[3].lstrip('"').rstrip('"'))
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()    
