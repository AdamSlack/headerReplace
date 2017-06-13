import unittest
from src.File import File


class FileUnitTests(unittest.TestCase):
    """ Unit tests for File Class """

    def test_cursor_assignment_via_setter_property_works(self):
        """ test the cursor assignment functions correctly """
        f = File()
        f.cursor_start = 1
        f.cursor_end = 1
        f.file_length = 20

        self.assertEqual(f.cursor_start, 0, msg='Zero Lines, cursor should reset to 0')
        self.assertEqual(f.cursor_end, 0, msg='Zero Lines, cursor should reset to 0')
        f.file_lines=['line: ' + str(i) for i in range(0,10)]
        self.assertEqual(f.file_length, 10, msg='Ten Lines, length should be 0')

    def test_cursor_assignment_does_not_exceed_bounds(self):
        """ testing that cursors don't overlap or exceed bounds """
        f = File()
        f.file_lines=['line: ' + str(i) for i in range(0,10)]
        f.cursor_end = 20
        f.cursor_start = 15

        self.assertEqual(f.file_length-1, f.cursor_end, msg='End cursor should match file length when bounds exceed')
        self.assertEqual(f.cursor_end, f.cursor_start, msg='start cursor should match end cursor when start overlaps')

        f.cursor_start = -10
        f.cursor_end = -5

        self.assertEqual(f.cursor_start, 0, msg='End cursor should match file length when bounds exceed')
        self.assertEqual(f.cursor_end, f.cursor_start, msg='end cursor should match start cursor when end overlaps')

        f.cursor_end = 4
        f.cursor_start = 2
        f.cursor_end = 1
        self.assertEqual(f.cursor_end, f.cursor_start, msg='end cursor should match start cursor when end overlaps')

    def test_file_lines_assignment_updates_file_length(self):
        """ test that file line assignment functions correctly."""
        f = File()

        self.assertEqual(f.file_length, 0, msg='Zero Lines, length should be 0')

        f.file_lines = ['line: ' + str(i) for i in range(0, 10)]
        self.assertEqual(len(f.file_lines), 10, msg='Ten Lines, length should be 0')
        self.assertEqual(f.file_length, 10, msg='Ten Lines, length should be 0')

    def test_strip_all_files_does_strips_all_files(self):
        """ """
        f = File()
        f.file_lines = [str(i) + ' squared is: ' + str(i*i) + '\n' for i in range(0, 100, 3)]
        other_lines = [str(i) + ' squared is: ' + str(i*i) for i in range(0, 100, 3)]
        f.rstrip_all_lines('\n')
        self.assertEqual(f.file_lines, other_lines, msg='all newlines should have been stripped.')


class FileFactoryTests(unittest.TestCase):
    """ Unit tests for FileFactory Class """


class ConfigSettingsTests(unittest.TestCase):
    """ Unit tests for ConfigSettings Class """


class ConfigHandlerTests(unittest.TestCase):
    """ Unit tests for ConfigHandler Class """


class ArgParserFactoryTests (unittest.TestCase):
    """ Unit tests for ArgParserFactory Class """


class Tests (unittest.TestCase):
    """ Unit tests for """

