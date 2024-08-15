# Plagiarism Detection

# Importing necessary libraries
import os
import re
import difflib

# Function to read file content
def read_file(file_path):
   with open(file_path, 'r') as file:
       content = file.read()
   return content

# Function to split code into tokens
def tokenize(code):
   tokens = re.findall(r"\w+|[^a-zA-Z\d\s]", code)
   return tokens

# Function to compare two files
def compare_files(file1, file2):
   content1 = read_file(file1)
   content2 = read_file(file2)
   
   tokens1 = tokenize(content1)
   tokens2 = tokenize(content2)
   
   diff = difflib.SequenceMatcher(None, tokens1, tokens2)
   similarity = diff.ratio()
   
   return similarity

# Function to compare a file with a directory
def compare_with_directory(file_path, directory_path):
   file_content = read_file(file_path)
   file_tokens = tokenize(file_content)
   
   similarities = []
   for filename in os.listdir(directory_path):
       if filename.endswith('.py'):
           file_path = os.path.join(directory_path, filename)
           similarity = compare_files(file_path, file_path)
           similarities.append((filename, similarity))
   
   return similarities

# Main function
def main():
   file_path = input("Enter the file path: ")
   directory_path = input("Enter the directory path: ")
   
   similarities = compare_with_directory(file_path, directory_path)
   
   print("Similarities:")
   for filename, similarity in similarities:
       print(f"{filename}: {similarity * 100:.2f}%")

# Initialize the program
if __name__ == "__main__":
   main()