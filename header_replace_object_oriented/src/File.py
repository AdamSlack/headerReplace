#
#   File Class
#


class File:
    """ File class - represents the a file on disk and the contents of it. """
    def __init__(self):
        """ Default Constructor each thing is default."""
        self.file_name = ''      # name of the file
        self._file_lines = []     # contents of the file
        self._file_length = 0     # number of lines in the file
        self._cursor_start = 0    # the line number of the start of the section to be replaced
        self._cursor_end = 0      # the line number of the end of the section to be replaced

    @classmethod  # Construct an File with information from a file.
    def PopulatedFile(cls, file_name='', file_lines=[], cursor_start=0, cursor_end=0):
        """ Parametrised constructor for a File. """
        file = File()

        file.file_name = file_name
        file.file_lines = file_lines
        file.cursor_start = cursor_start
        file.cursor_end = cursor_end

        return file

    #
    # @classmethod # construct a blank file with information from a file
    #

    # Cursor Start Access Properties
    @property
    def cursor_start(self):
        return self._cursor_start

    @cursor_start.setter
    def cursor_start(self, line_number):
        """ Set the start cursor to point at the specified line. """
        self._cursor_start = line_number
        if self._cursor_start < 0:
            self._cursor_start = 0

        if self._cursor_start > self.cursor_end:
            self._cursor_start = self.cursor_end

    #
    # Cursor End Access Properties
    #
    @property
    def cursor_end(self):
        return self._cursor_end

    @cursor_end.setter
    def cursor_end(self, line_number):
        """ Set the start cursor to point at the specified line. """
        self._cursor_end = line_number
        if self._cursor_end > self.file_length - 1:
            self._cursor_end = self.file_length - 1

        if self._cursor_end < self.cursor_start:
            self._cursor_end = self.cursor_start

    #
    # File Length Access Properties
    #
    @property
    def file_length(self):
        return self._file_length

    @file_length.setter
    def file_length(self, value):
        self._file_length = len(self.file_lines)

    #
    # File Lines access properties
    #
    @property
    def file_lines(self):
        return self._file_lines

    @file_lines.setter
    def file_lines(self, file_lines):
        self._file_lines = file_lines
        self.file_length = len(file_lines)

        # if end cursor exceeds max index of file_lines
        if self.cursor_end > self.file_length - 1:
            self.cursor_end = self.file_length - 1

        # if  start cursor exceeds max index of file_lines
        if self.cursor_start > self.file_length - 1:
            self.cursor_start = 0

    #
    # Other Member methods.
    #
    def selection_length(self):
        """ returns the number of lines between and including the cursor's start and end position """
        return self.cursor_end - self.cursor_start + 1

    def rstrip_all_lines(self, regex=''):
        """ strip an expression from all lines in the file """
        self.file_lines = [l.rstrip(regex) for l in self.file_lines]

    def flush_contents(self, dir_path):
        """ flush the contents of this file to disk """
        f = open(dir_path + '/' + self.file_name, 'w')
        f.writelines(self.file_lines)