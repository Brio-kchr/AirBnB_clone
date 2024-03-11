#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
#from models.engine.file_storage import FileStorage
from models import storage
""""this module holds the console program"""


class HBNBCommand(cmd.Cmd):
    """ Classs to handle the command interpreter
    """
    prompt = "(hbnb) "
    classes = ["BaseModel"]

    def do_quit(self, arg):
        """ To quit from  the console
        """
        return True

    def do_EOF(self, line):
        """"Exits the Console
        """
        return True

    def do_create(self, arg):
        """
        creates a new instance of basemodel, saves
        it json file and prints the id.
        """
        if arg:
            args = arg.split()
            if args[0] in self.classes:
                if args[0] == "BaseModel":
                    obj = BaseModel()
                    obj.save()
                    print("{}".format(obj.id))
            else:
                print("{}".format("** class doesn't exist **"))
        else:
            print("{}".format("** class name missing **"))

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id.
        """
        if arg:
            args = arg.split()
            if args[0] not in self.classes:
                print("{}".format("** class doesn't exist **"))
            else:
                if args[1]:
                    # Get all the objects
                    all_objects = storage.all()
                    object_key = "{}.{}".format(args[0], args[1])
                    if object_key in all_objects:
                        print(all_objects[object_key])
                    else:
                        print("** no instance found **")
                else:
                    print("{}".format("** instance id missing **"))

        else:
            print("{}".format("** class name missing **"))

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        Saves changes into the JSON file
        """
        if arg:
            args = arg.split()
            if args[0] not in self.classes:
                print("{}".format("** class doesn't exist **"))
            else:
                if args[1]:
                    # Destroy based on name
                    all_objects = storage.all()
                    object_key = "{}.{}".format(args[0], args[1])
                    if object_key in all_objects:
                        del all_objects[object_key]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
        else:
            print("{}".format("** class name missing **"))

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        all_objects = storage.all()
        if arg:
            args = arg.split()
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                for key, value in all_objects.items():
                    if key.split('.')[0] == args[0]:
                        print(str(value))
        else:
            for key, value in all_objects.items():
                # Either prints all values
                # print(str(value))
                print(str(all_objects[key]))

    def do_update(self, arg):
        """

        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
