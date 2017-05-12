#
# Controller Class
#
from src.ArgParserFactory import ArgParserFactory
from src.ConfigHandler import ConfigHandler
from src.FileFactory import FileFactory
from src.DirectoryFactory import DirectoryFactory
from src.Model import Model


class Controller:
    """ MVC Controller Class """

    def __init__(self):
        """ Controller Class constructor """
        # Cmd Line Argument Setup
        self.arg_parser = ArgParserFactory.create_arg_parser()
        self.args = self.arg_parser.parse_args()

        # Config File Setup
        self.config_handler = ConfigHandler()
        self.config_settings = self.config_handler.read_config('../config/config.json')

        # File Factory
        self.file_factory = FileFactory
        self.directory_factory = DirectoryFactory
        # Empty Model
        self.model = Model()

    def read_arg_file(self, path):
        """ get the list of directories from the location specified at the cmd line """
        file_from_arg = FileFactory.create_file(path)
        return file_from_arg

    def populate_model(self):
        """ populates model with files found in the directory specified in args """
        dir_file = self.read_arg_file(self.args.dir_file)
        replacement_file = self.read_arg_file(self.args.dir_file)

        self.model.replacement_file = replacement_file
        for dir_path in dir_file.file_lines:
            new_dir = self.directory_factory.create_directory(dir_path)
            self.model.dirs[new_dir.dir_name] = new_dir
