#
#  Model Class
#
from src.File import File

class Model:
    """ MVC Model Class"""

    def __init__(self):
        """ Model Class Constructor """
        self.replacement_file = File()
        self.dirs = {}
        self.dir_count = 0

    def add_dir(self, new_dir):
        """ Add a dir to the model's map of Directories"""
        self.dirs[new_dir.dir_name] = new_dir
        self.dir_count = len(self.dirs)

    def get_dir(self, dir_name):
        """ return a directory object from the model's map of directories"""
        return self.dirs[dir_name]

    def remove_dir(self, dir_name):
        """ remove a directory object from the model's map of directories """
        del self.dirs[dir_name]

    def add_file(self, dir_name, the_file ):
        """ add a file to a specified dir in the model's map """
        self.dirs[dir_name].files[the_file.file_name] = the_file
