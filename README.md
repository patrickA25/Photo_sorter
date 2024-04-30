# Photo Sorter

## Overview
Photo Sorter is a simple Python script that helps organize files in a directory by sorting them into subfolders based on their file extension. This tool is especially useful for managing large directories, making them easier to navigate and maintain.

## Features
- **Automated Sorting:** Automatically sorts files into appropriately named subfolders based on their file extension.
- **Easy to Use:** Run the script from the terminal—no complex setup required.

## Installation

### Prerequisites
- Python 3.x

### Setup
1. Clone this repository or download the script directly:
   ```bash
   git clone https://github.com/yourusername/photo-sorter.git

## Usage
To use Photo Sorter, you will need to run the script from the terminal and specify the path to the directory
containing the files you want to sort. Here is the command format. 

```bash
python photo_sorter.py /path/to/your/directory
```
Replace `/path/to/your/directory` with the actual path to the directory where your files are located.


## Contributing
Contributions are welcome! If you have improvements or bug fixes, please feel free to fork the repository and submit a pull request.

## Function Overview

```python
def get_file_extension(folder_location):
    """This function will return a list of unique file extensions
        that are in the folder location.

    Args:
        folder_location (String): The location of the folder that
        contains all of the pictures you want sorted.

    Returns:
        List: A list of all of the unique file extension that can be
        found inside of the folder_location
    """
    os.chdir(str(folder_location))
    file_list = os.listdir()
    extensionList = []
    for pic in file_list:
        file_list_split = os.path.splitext(pic)
        extensionList.append(file_list_split[1])
    return list(set(extensionList))
```

```python
def creating_directories(folder_location,extension_list):
    """This function will create a new directory for each extension 
    in the extension_list.

    Args:
        folder_location (String): The location of the folder that
        contains all of the pictures you want sorted.
        
        extension_list (List): A list of all file extension you 
        want to have moved into a seperate folder.
    """
    os.chdir(folder_location)
    for new_folder in extension_list:
        folder_name = str(new_folder) + "_Pictures"
        new_path = os.path.join(folder_location,folder_name)
        os.mkdir(new_path)
```

```python
def moving_pictures(folder_location,extension_list):
    """This function will iterate through the directory moving all
        pictures with an extension in teh extension_list to a new directory.

    Args:
        folder_location (String): The location of the folder that
        contains all of the pictures you want sorted.
        
        extension_list (List): A list of all file extension you 
        want to have moved into a seperate folder.    """
    os.chdir(folder_location)
    file_list = os.listdir()
    for file in file_list:
        file_list_split = os.path.splitext(file)
        if file_list_split[1] in extension_list:
            print(file_list_split)
            old_path = os.path.join(folder_location,file)
            new_path = os.path.join(folder_location,str(file_list_split[1]) + "_Pictures\\"+file)
            os.rename(old_path,new_path)
````

## License

MIT License
