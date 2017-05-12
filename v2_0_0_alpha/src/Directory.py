#
#   Directory class
#


class Directory:
    """ Directory Class - Map of Files in a given directory. """

    def __init__(self):
        """ default constructor """
        self.files = {}
        self.file_count = 0
        self.dir_path = ''
        self.dir_name = ''

    def flush_directory_contents(self):
        """ flush each file to disk """
        for f in self.files:
            f.flush_contents()

