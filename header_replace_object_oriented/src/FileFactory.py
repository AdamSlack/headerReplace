#
# Class for the construction of File Objects
#
from src.SASFile import SASFile
from src.File import File


class FileFactory:
    """ Class for the construction of File Objects"""

    def __init__(self):
        """ doesn't do anything really..."""

    @staticmethod
    def create_file(file_path):
        """ creates plain file object. """

        f = open(file_path)
        file_lines = f.readlines()
        line_count = len(file_lines)

        return File.PopulatedFile('dir_file', file_lines, 0, line_count - 1 )


    @staticmethod
    def create_sas_file(directory, file_name):
        """ creates a File object from the file found at the specified location """

        if directory[-1] == '/':
            directory = str.rstrip(directory, '/')
        file_path = directory + '/' + file_name
        return SASFile()
