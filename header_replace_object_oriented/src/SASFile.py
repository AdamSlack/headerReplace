#
# SASFile - File derived Class
#

from .File import File


class SASFile(File):
    """ SASFile Derived Class """

    def __init__(self):
        """ Class Constructor"""
        File.__init__(self)  # Base Class Constructor Call


