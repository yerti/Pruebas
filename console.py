#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """text"""
    def emptyline(self):
        """text"""
        pass

    completekey = None
    prompt = '(hbnb)'

    def __init__(self):
        super().__init__()

    def do_help(self, line):
        """Show help information for commands"""
        print("\n")
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF  help  quit  create")
        print("\n")

    def help_help(self):
        """text"""
        print("Show help information for commands")

    def do_quit(self, line):
        print("Quit command to exit the program")
        return True

    def do_EOF(self, line):
        return True

    def do_create(self, line):
        """text"""
        if not line:
            print("** class name missing **")
        else:
            from models.base_model import BaseModel
            try:
                cls = eval(line)
                instance = cls()
                instance.save()
                print(instance.id)
            except NameError:
                print("** class doesn't exist **")
    
    def do_show(self, line):
        """text"""
        if not line:
            print("** class name missing **")
        else:


if __name__ == '__main__':
    HBNBCommand().cmdloop()
