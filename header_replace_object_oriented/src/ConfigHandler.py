#
# Config Handler Class
#
import json
from src.ConfigSettings import ConfigSettings


class ConfigHandler:
    """ Class to handle config files """

    def __init__(self):
        """ class constructor """
        self.config_contents = {}

    def read_config(self, file_path):
        """ parses config file in json format"""

        config_file = open(file_path)
        self.config_contents = json.load(config_file)
        config_file.close()

        return self.config_contents

    def create_config_settings(self, file_path):
        """ returns a ConfigSettings object constructed from config_contents"""
        self.config_contents = self.read_config(file_path)
        # create empty config file object
        cs = ConfigSettings()

        # populate logfile related config settings
        logfile_config = self.config_contents.get('logfile')
        cs.logfile_file_name = logfile_config.get('file_name')
        cs.logfile_date_stamp_file_name = logfile_config.get('date_stamp_file_name')
        cs.logfile_time_stamp_file_name = logfile_config.get('time_stamp_file_name')
        cs.logfile_save_location = logfile_config.get('save_location')

        # populate sccs related config settings
        sccs_config = self.config_contents.get('sccs')
        cs.sccs_check_in_message = sccs_config.get('check_in_message')

        # populate version history related config settings
        version_config = self.config_contents.get('version_history')
        cs.version_history_clear_history = version_config.get('clear_message')
        cs.version_history_message = version_config.get('clear_history')

        # return populated Config Settings file.
        return cs
