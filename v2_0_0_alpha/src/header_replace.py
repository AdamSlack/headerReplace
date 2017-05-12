#
#   Main
#

from src.ConfigHandler import ConfigHandler
from src.Controller import Controller

def main():
    """ Main. """
    cf = ConfigHandler()
    cs = cf.create_config_settings('../config/config.json')

    c = Controller()

    f = c.get_dir_file()


if __name__ == '__main__':
    main()