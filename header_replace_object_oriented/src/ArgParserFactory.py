#
#   Arg parser factory class
#   Probably not needed at all...
#
from argparse import ArgumentParser

class ArgParserFactory:
    """ Class for creating an Arg Parser """

    @staticmethod
    def create_arg_parser():
        """ creates a CMD line argument parser with possible options """
        parser = ArgumentParser(description='Replaces Header section of Amgen standard .SAS files.')
        #group = parser.add_mutually_exclusive_group(required=True)

        parser.add_argument('-d', '--dir_file',
                           help='Path of the [d]irectory paths .txt file, containing the paths to that need' +
                                'headers to be replaced',
                           required=True)

        parser.add_argument('-r', '--replacement_file',
                            help='Path of the .txt file containing the text that is used as the replacement content',
                            required=True)

        parser.add_argument('-v', '--version_history',
                            help='Wipe the [v]ersion history present in the header.',
                            action='store_true')

        return parser
