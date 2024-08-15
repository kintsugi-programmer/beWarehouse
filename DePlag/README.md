# Plagiarism Detection

This program is designed to detect plagiarism in a given file by comparing it with all the files in a specified directory. It calculates the similarity between the target file and each file in the directory using a token-based comparison method.

## Features

- Read the content of a file
- Split code into tokens (words and special characters)
- Compare two files based on their token sequences
- Compare a file with all files in a directory
- Display the similarities between the file and each file in the directory

## Usage

1. Run the script
2. Enter the file path of the target file when prompted
3. Enter the directory path containing the files to be compared when prompted
4. The program will display the similarities between the target file and each file in the directory

## Implementation Details

### Libraries Used

- `os`: For file and directory operations
- `re`: For regular expressions
- `difflib`: For comparing sequences

### Functions

#### `read_file(file_path)`

- **Description:** Reads the content of a file
- **Parameters:**
  - `file_path` (str): The path of the file to be read
- **Returns:**
  - `content` (str): The content of the file

#### `tokenize(code)`

- **Description:** Splits the code into tokens (words and special characters)
- **Parameters:**
  - `code` (str): The code to be tokenized
- **Returns:**
  - `tokens` (list): A list of tokens

#### `compare_files(file1, file2)`

- **Description:** Compares two files based on their token sequences
- **Parameters:**
  - `file1` (str): The path of the first file
  - `file2` (str): The path of the second file
- **Returns:**
  - `similarity` (float): The similarity ratio between the two files

#### `compare_with_directory(file_path, directory_path)`

- **Description:** Compares a file with all the files in a directory
- **Parameters:**
  - `file_path` (str): The path of the target file
  - `directory_path` (str): The path of the directory containing files to be compared
- **Returns:**
  - `similarities` (list): A list of tuples containing the filename and similarity ratio

#### `main()`

- **Description:** The entry point of the program
- **Functionality:**
  - Prompts the user to enter the file path and directory path
  - Calls the `compare_with_directory` function with the provided paths
  - Prints the similarities between the file and each file in the directory

### Classes and Structures

This implementation does not use any custom classes or structures. However, it utilizes built-in data structures such as lists and tuples for storing and manipulating data.

### Main Program Flow

1. The `main` function is called when the script is run.
2. The user is prompted to enter the file path and directory path.
3. The `compare_with_directory` function is called with the provided paths.
4. The similarities between the target file and each file in the directory are printed.