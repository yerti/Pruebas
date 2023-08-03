#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """text"""
    completekey = None
    
    prompt = '(hbnb) '

    def __init__(self):
        super().__init__()

    def do_help(self, line):
        """Show help information for commands"""
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF  help  quit")

    def help_help(self):
        """text"""
        print("Show help information for commands")

    def do_quit(self, line):
        print("Quit command to exit the program")
        return True

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
