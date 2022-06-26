import os
import sys
import lib.photoSortingFunctions as photoSortingFunctions



def main(dir_location):
    print(photoSortingFunctions.get_file_extension(dir_location))
    extension_list = []
    extension_list = [item for item in input("Enter the extension you would like to move : ").split()]
    print(f"All files with {extension_list} extension will be moved")
    photoSortingFunctions.creating_directories(dir_location,extension_list)
    photoSortingFunctions.moving_pictures(dir_location,extension_list)

if __name__ == "__main__":
    main(sys.argv[1])