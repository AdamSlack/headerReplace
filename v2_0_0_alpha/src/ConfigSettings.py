#
#  Config Settings Class
#


class ConfigSettings:
    """ Class to encapsulate config settings """

    def __init__(self):
        """ class constructor """
        self.logfile_save_location = ''
        self.logfile_file_name = ''
        self.logfile_date_stamp_file_name = True
        self.logfile_time_stamp_file_name = True

        self.sccs_check_in_message = ''

        self.version_history_message = ''
        self.version_history_clear_history = ''

