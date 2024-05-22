#!/usr/bin/python3
"""
Main entry of the AirBnB project
a command prompt using the cmd
an (hbnb) prompt loop
defines methods and takes the user command
using the python commanline arguments
kwargs and args
this is gonna be fun!!
"""

import cmd
import models
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """
    Command prompt to get user commands
    """
    prompt = '(hbnb) '
    __classes = [
        "Amenity",
        "BaseModel",
        "City",
        "Place",
        "Review",
        "State",
        "User"
    ]

    def do_quit(self, args):
        """ user enter 'quit'to exit the program"""
        return True

    def do_EOF(self, args):
        """ctrl + c to quit the program """
        return True

    def emptyline(self):
        """ if an empty line is entered
        do nothing
        """
        pass

    def do_create(self, args):
        """
        Create a new instance of BaseModel, save it and prints the id
        Usage: create <class name>
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            create_class = eval(args[0] + '()')
            models.storage.save()
            print(create_class.id)

    def do_show(self, args):
        """
        method that displays  the string representation
        of a specific instance
        Usage: show <class name> <id>
        """
        words = args.split()
        if len(words) == 0:
            print("** class name missing **")
        elif words[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(words) == 1:
            print("** instance id missing **")
        else:
            obj = models.storage.all()
            kv = words[0] + '.' + words[1]
            if kv in obj:
                print(obj[kv])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """
        method to Delete an instance
        Usage: destroy <class name> <id>
        """
        args = args.split()
        objects = models.storage.all()

        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            search_key = args[0] + "." + args[1]
            if search_key in objects.keys():
                objects.pop(search_key, None)
                models.storage.save()
            else:
                print('** no instance found **')

    def do_all(self, args):
        """
        method that displays str representation of all instances
        Usage: all <class name>
        """
        args = args.split()
        objects = models.storage.all()
        new_list = []

        if len(args) == 0:
            for obj in objects.values():
                new_list.append(obj.__str__())
            print(new_list)
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for obj in objects.values():
                if obj.__class__.__name__ == args[0]:
                    new_list.append(obj.__str__())
            print(new_list)

    def do_update(self, args):
        '''
        method that Updates an instance
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        '''
        objects = models.storage.all()
        args = args.split(" ")

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            kf = args[0] + '.' + args[1]
            obj = objects.get(kf, None)

            if not obj:
                print("** no instance found **")
                return

            setattr(obj, args[2], args[3].lstrip('"').rstrip('"'))
            models.storage.save()

    def check_class_name(self, name=""):
        """
        method to check for class name.
        """
        if len(name) == 0:
            print("** class name missing **")
            return False
        else:
            return True

    def check_class_id(self, name=""):
        """ Check class id."""
        if len(name.split(' ')) == 1:
            print("** instance id missing **")
            return False
        else:
            return True

    def found_class_name(self, name=""):
        """method to find the class name """
        if self.check_class_name(name):
            args = shlex.split(name)
            if args[0] in HBNBCommand.__classes:
                if self.check_class_id(name):
                    key = args[0] + '.' + args[1]
                    return key
                else:
                    print("** class doesn't exist **")
                    return None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
