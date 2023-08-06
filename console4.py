#!/usr/bin/python3
"""class console interactive"""

import shlex
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    
    def do_all(self, arg):
        """Creates a new instance of BaseModel"""

        args = arg.split()
        if not arg:
            print([str(v) for v in storage.all().values()])
        elif args[0] in ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']:
            print([str(v) for v in storage.all(eval(args[0])).values()])
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""

        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj = storage.all().get(key)
            if obj:
                print(obj)
            else:
                print("** no instance found **")

    def do_create(self, arg):
        """Creates a new instance of a class"""

        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']:
            print("** class doesn't exist **")
        else:
            obj = eval(args[0])()
            obj.save()
            print(obj.id)

    def do_destroy(self, arg):
        """Deletes an instance based on the class"""

        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objs = storage.all()
            if key in objs:
                del objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance based on the class"""

        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objs = storage.all()
            if key not in objs:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                setattr(objs[key], args[2], args[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
