from headerReplace import *
import unittest


# findExpression() Test Cases
class FindExpressionTests(unittest.TestCase):
    """ A Series of methods designed to test the functionality of FindExpression in the 'header replace' script """

    def test_findExpression_emptyLines(self):
        """ Sanity check that 'findExpression' returns -1 when array of strings is empty """
        emptyLines = []
        expression = "Expression"
        result = findExpression(emptyLines, expression)
        self.assertEqual(result, -1)

    def test_findExpression_emptyExpression(self):
        """ Sanity check that 'findExpression' returns -1 when an empty string is used as search expression """
        lines = ["Line 0", "Line 1", "Line 2", "Line 3"]
        emptyExpression = ""
        result = findExpression(lines,emptyExpression)
        self.assertEqual(result, -1)

    def test_findExpression_findsFirstOf(self):
        """ Test that 'findExpression' returns the line number of the first instance of an expression """
        lines = ["Line 0", "Line 1", "Line 2", "Line 3"]
        expression = "Line"
        result = findExpression(lines, expression)
        self.assertEqual(result, 0)

    def test_findExpression_findsEmbeddedExpression(self):
        """ Test that 'findExpression' will find an expression regardless of the surrounding text. """
        lines = ["This is Line Number 0", "Line 1", "Line 2", "Line 3"]
        expression = "in"
        result = findExpression(lines, expression)
        self.assertEqual(result, 0)


# listAvailableFiles() Test Cases
class ListAvailableFilesTests(unittest.TestCase):
    """ A Series of methods designed to test the functionality of ListAvailableFiles in the 'header replace' script """

    def test_listAvailableFiles_emptyDir(self):
        """ test that 'listAvailableFiles' returns an empty list when presented with an empty directory """
        files = listAvailableFiles('testFiles/emptyDir')
        self.assertEqual(len(files), 0)

    def test_listAvailableFiles_mixedDir(self):
        """ test that 'listAvailableFiles' returns the file name of only those matching extension """
        files = listAvailableFiles('testFiles/mixedFiles', '.sas')
        self.assertEqual(len(files), 3)

    def test_listAvailableFiles_allMatchingDir(self):
        """ test that 'listAvailableFiles' returns all files in a dir"""
        files = listAvailableFiles('testFiles/mixedFiles', '.sas')
        self.assertEqual(len(files), 3)

    def test_listAvailableFile_nonExistantDir(self):
        """ Test of 'listAvailableFile' when presented with a directory path that doesn't exist. """
        files = listAvailableFiles('madeUpDIR')
        result = len(files)
        self.assertEqual(result, 0)

    def test_listAvailableFile_noDirSpecified(self):
        """ Test of 'listAvailableFile' when provided with an empty String for a DIR """
        files = listAvailableFiles('')
        result = len(files)
        self.assertEqual(result, 0)


# readFile() Test Cases
class ReadFileTests(unittest.TestCase):
    """ A Series of methods designed to test the functionality of ReadFile in the 'header replace' script """

    def test_readFile_emptyFile(self):
        """ test of 'readFile' when presented with an empty file """
        lines = readFile("testFiles/sasFiles/a.sas")
        result = len(lines)
        self.assertEqual(result, 0)

    def test_readFile_knownLineCount(self):
        """ test of 'readFile' when presented with a file of a known file count. """
        lines = readFile("testFiles/sasFiles/b.sas")
        result = len(lines)
        self.assertEqual(result, 7)

    def test_readFile_nonExistantFile(self):
        """ test of 'readFile' when presented with a filePath to a non-existant file """
        lines = readFile("noteReal.txt")
        result = len(lines)
        self.assertEqual(result, 0)

    def test_readFile_invalidFileName(self):
        """ test of 'readFile' wjhen presented with an invalid filepath. """
        lines = readFile("")
        result = len(lines)
        self.assertEqual(result, 0)


# WriteFile() Test Cases
class WriteFileTests(unittest.TestCase):
    """ A Series of methods designed to test the functionality of WriteFile in the 'header replace' script """

    def test_writeFile_knownFileLength(self):
        """ check the resultant length of a file after writing new contents to it.  """
        lines = ["1\n", "2\n", "3\n", "4"]
        writeFile('testFiles/fileWriting/testFile.txt', lines)
        result = len(readFile('testFiles/fileWriting/testFile.txt'))
        self.assertEqual(result, 4)

    def test_writeFile_emptyfile(self):
        """ check that an empty file remains empty when written to """
        lines = []
        writeFile('testFiles/fileWriting/testFile.txt', lines)
        result = len(readFile('testFiles/fileWriting/testFile.txt'))
        self.assertEqual(result, 0)

    def test_writeFile_newFile(self):
        """ test that a file is created if it doesn't already exist """
        try:
            os.remove('testFiles/fileWriting/missing.txt')
        except FileNotFoundError:
            """ """
        else:
            """ """
        lines = []
        writeFile('testFiles/fileWriting/missing.txt', lines)
        result = len(readFile('testFiles/fileWriting/missing.txt'))
        self.assertEqual(result, 0)
        os.remove('testFiles/fileWriting/missing.txt')

    def test_writeFile_overwriteFile(self):
        """ test that a file is overwritten if it already exists. """
        

########################################################
#                                                      #
#                        Main                          #
#                                                      #
########################################################
if __name__ == '__main__':
    unittest.main()