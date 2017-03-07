########################################################################################################################
#                                                                                                                      #
#                                               Header Replace Script                                                  #
#                                                                                                                      #
########################################################################################################################
#                                                                                                                      #
#   This script is used to update the top part of a header in all .SAS files found within a specified directory.       #
#   The purpose of this is to ensure that the header used across all files in a study is consistent and up to date     #
#   with the current standard.                                                                                         #
#                                                                                                                      #
#   Should the standard change this script can be used to update all in a given directory to reflect this change.      #
#                                                                                                                      #
#   To use this script ensure that this .py file has the header(.txt) file that is to be used present in the same      #
#   directory. if there is no header available for this script to use, then it will fail. no changes to files will be  #
#   made.                                                                                                              #
#                                                                                                                      #
#   this program will not alter anything in the SAS files, BESIDES the top section of the header. The top section      #
#   currently begins with a line that starts '/*===========' and ends with the first line that starts '___________'    #
#   should this change, then the script will need updating.                                                            #
#                                                                                                                      #
#                           <Insert some README stuff about the cmd line args and stuff...>                            #
#                                                                                                                      #
########################################################################################################################
#                                                                                                                      #
#   For any questions, queries or errors that have occurred as a result of this script, please email me and i shall    #
#   get it sorted!                                                                                                     #
#                                                                                                                      #
########################################################################################################################
import os, argparse

# Needs to be turned into an object...
histNeeded = False


def listAvailableFiles(directory, suffix='.sas'):
    """ Creates a list of all files that exist within a directory that are readable """
    readableFiles = []

    try: # Try listing files in a directory.
        dirList = os.listdir(directory)
    except FileNotFoundError: # don't break if the dir provided is not found
        print('Invalid Directory Specified')
    else: # if it's good, continue as planned
        for file in dirList:
            if file.endswith(suffix) and os.access(directory + "\\" + file, os.R_OK):  # i.e. the file can be checked.
                readableFiles.append(file)

        print(str(len(readableFiles)) + ' files located.')

    return readableFiles


# should get around SCCS... 100% shouldn't be done this way...
def setPermissions(directory, files):
    """ sets the permissions of all files to 777 """
    for file in files:
        os.chmod(directory + "\\" + file, 0o777)  # gives write access so files can be edited


def readFile(filePath):
    """ reads a file, returning an array of lines in the file """
    lines = []      # or even lines = [l for l in file]
    try:
        file = open(filePath)
    except FileNotFoundError:
        print("Invalid File Path Provided")
    else:
        for l in file:
            lines.append(l)
    return lines


def findExpression(lines, expr, startPos=0):
    """ Searches an array of strings for an expression. returning the line idx that contains it"""
    idx = -1
    if expr == "":
        return idx

    for i in range(startPos, len(lines)):
        if expr in lines[i]:
            idx = i
            break  # Line is found, bail from the loop.
    return idx


def updateFile(original, header, startIdx, endIdx):
    """ creates a new file with an updated header, then returns it """
    newFile = []

    for i in range(startIdx):  # keep the segment occurring before the start idx
        newFile.append(original[i])

    newFile.extend(header)  # add to the new file with the desired header

    for i in range(endIdx + 1, len(original)):  # place the rest of the original file that is needed
        newFile.append(original[i])
    return newFile


def writeFile(filePath, file):
    """ writes a file at the specified location """
    f = open(filePath, 'w')  # Create a blank version of the original file
    for l in file:  # Write the new lines to the blank file.
        f.write(l)
    f.close()


def updateHeaders(directory, headerFile, startExp =  "/*====", endExp = "_______"):
    """ goes through all sas files in a directory and updates their headers """
    global histNeeded
    print('Updating headers for files in: ' + directory)

    header = readFile(headerFile)
    fileNames = listAvailableFiles(directory)
    setPermissions(directory, fileNames)

    for f in fileNames:  # go through each file in the directory.
        path = directory + "\\" + f
        fileLines = readFile(path)
        start = findExpression(fileLines, startExp)  # used to mark the start of the area to replace

        if start == -1:
            break  # the start of the header was not found. Skip this file since it's not valid. don't wanna ruin stuff

        end = findExpression(fileLines, endExp, startPos=start)  # used to mark the end of the area to replace
        newFile = updateFile(fileLines, header, start, end)

        if histNeeded:  # This needs to be done better. too many branches.
            start = findExpression(newFile, "Version History")
            versionHist = readFile('verHist.txt')
            if start != -1:
                end = findExpression(newFile, "====*/")
                newFile = updateFile(newFile, versionHist, start, end)

        writeFile(path, newFile)

    print('Headers Updated.\n')


def createArgParser():
    """ creates a CMD line argument parser with possible options """
    parser = argparse.ArgumentParser(description='Replaces Header section of Amgen standard .SAS files.')
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('-d', '--dir',
                       help='The [d]irectory location of files needing to have headers replaced')

    group.add_argument('-m', '--multiple',
                       help='Location of the .txt file containing the paths to [m]ultiple directories that need' +
                            'headers to be replaced')

    parser.add_argument('-f', '--file',
                        help='Location of the .txt header [f]ile containing the new header\'s content',
                        required=True)

    parser.add_argument('-v', '--versionhistory',
                        help='Wipe the version history present in the header.',
                        action='store_true')

    return parser


def updateDirs(filePath, headerFile):
    """ Updates the headers for each file located in each Directory located in the given file."""
    dirs = readFile(filePath)

    # OUTPUT FOR USER.
    print(str(len(dirs)) + ' directory locations read in the file:\n' + filePath + '\n')

    for d in dirs:
        updateHeaders(d.strip('\n'), headerFile)

    print('Directories Updated')


########################################################################################################################
#                                                                                                                      #
#                                                          Main                                                        #
#                                                                                                                      #
########################################################################################################################

def main():
    """ Main """
    global histNeeded
    parser = createArgParser()
    vars = parser.parse_args()

    print('\nUsing the contents of header file:\n' + vars.file + '\n')

    histNeeded = vars.versionhistory

    header = vars.file
    if vars.dir is not None:
        updateHeaders(vars.dir, header)
    elif vars.multiple is not None:
        updateDirs(vars.multiple, header)

if __name__ == '__main__':
    main()
