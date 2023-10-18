import os
import sys


class FilenamesExtractor():
    """
    ## Filenames extractor
    Extracts names of all files and folders from a given directory in a text file
    """

    def extract(self, directory: str):
        """extracts the names of each file and folder from the given 'directory'"""

        # raise error if directory doesn't exists
        if not os.path.exists(directory):
            raise ValueError()

        # raise error if directory is a file path
        if os.path.isfile(directory):
            raise NotADirectoryError()

        # get (directory)'s basename & drive letter
        basename = os.path.basename(directory)
        drivename = os.path.splitdrive(directory)[0].replace(":", "")

        # generate a non-existing name for text file
        filename = self.filename_increment(
            f"{drivename} - '{basename}' Files List.txt")

        """Extracting and Writing Process"""
        # Create and open a text file to write the data
        with open(filename, "w") as textfile:
            # scan the directory
            for folder, subfolders, files in os.walk(directory):
                try:
                    # write folder paths
                    textfile.write(f"\nFolder path: {folder}\n")
                    textfile.write(
                        f"Folder name: {os.path.basename(folder)}\n")

                    # Also list 'subfolders' from 'folder' in textfile
                    """
                    for subfolder in subfolders:
                        textfile.write(f"   > Subfolder: {subfolder}\n")
                    """

                    # loop through all 'files'
                    for f in files:
                        try:
                            # write filename
                            textfile.write(f"   > File: {f}\n")

                        # if filename is invalid, leave a helper message
                        except UnicodeEncodeError:
                            textfile.write(
                                "   > File: *** Invalid filename, try changing it ***\n")
                            pass

                # if folder name invalid,
                except UnicodeEncodeError:
                    textfile.write(
                        "\nFolder path: *** Invalid foldername, try changing it ***")
                    pass

        # return the name of newly created text file also
        return filename

    def filename_increment(self, filename: str):
        """Increments a filename if it already exists, returns the same name otherwise

        Creates a new name with an incremented number at the -
        end (before extension)
        """

        # new name
        new_name = filename
        # factoring out the name (without ext.) from 'filename'
        name = filename.split(".")[0]

        # if default name already exists
        if os.path.exists(new_name):
            # range(1000) means there can be 1000 incrementations only!
            for i in range(1000):
                # create new name with 'i' number at the end (before ext.)
                new_name = f"{name}-{i}.txt"

                # if new name doesn't exists
                if not os.path.exists(new_name):
                    # return the new name
                    return new_name
        else:
            # return the same name otherwise
            return new_name


def main():
    # executing the project
    fe = FilenamesExtractor()

    while True:
        try:
            # target dir address
            directory = input("Enter a directory (ctrl+c to exit): ")

            # extract all names from the given directory
            f = fe.extract(directory)

            print(f"\nExtracted data in: {f} \n")

        # if given string is a filepath
        except NotADirectoryError:
            print("*** Invalid directory ***\n")
            continue

        # if given path is not an existing directory
        except ValueError:
            print("*** Directory does not exists ***\n")
            continue

        # quit on ctrl+c
        except KeyboardInterrupt:
            sys.exit()


if __name__ == "__main__":
    main()

"""
Algorithm: How it works?

Take a directory
create and open a text file (to write data)
loop through every folder, subfolder and file in the 
    directory given using `os.walk()`
write folder name in the file
loop through each file and write its name


---------------------------
TODO Add more features:
    Feature: Time it took to extract data
    Feature: How much folders and files extracted
    Feature: Name of the .txt file in which data is extracted
    Feature: Size of that .txt file
    Feature: 

"""
