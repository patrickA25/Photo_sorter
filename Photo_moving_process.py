import os
import lib.photoSortingFunctions



def main():
    photoSortingFunctions.get_file_extension("direcetory_location")
    photoSortingFunctions.creating_directories("Directory_location",['.JPG','.SRW'])
    photoSortingFunctions.moving_pictures("directory_location",['.JPG','.SRW'])

if __name__ == "__main__":
    main()