#
#   Directory Factory
#
from src.FileFactory import FileFactory


class DirectoryFactory:

    def __init__(self):
        """ default constructor"""
        self.file_factory = FileFactory()

    def create_directory(self, dir_path):
        """ create a directory of File objects from a specified path."""

