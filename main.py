# << GOALS >>
# Traverse a directory
# For each file, collect & store metadata 
# Add search functionality

import os #for file navigation
import time #for last modified
import json #for metadata storage

test_dir = r"C:\Users\itspebbleboy\Documents\GitHub\File-Metadata-Search-Tool-Python\test_folder"
test_file = r"C:\Users\itspebbleboy\Documents\GitHub\File-Metadata-Search-Tool-Python\test_folder\file.txt"

#func, scans a directory & prints paths of all files
def scan_directory(directory):
    #walk thru directories & subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files: #iter thru all files in curr dir
            file_path = os.path.join(root,file)
            print(file_path) #print full file path of ea file

#test printing functionality w/ test folder
scan_directory(test_dir)

#############

# function, gets metadata of file
def get_file_metadata(file_path):
    stats = os.stat(file_path) #get file stats
    return{
        "name": os.path.basename(file_path), #file name from path
        "size": stats.st_size, # file size (bytes)
        "type": os.path.splitext(file_path)[1], #file extension
        "last_modified": time.ctime(stats.st_mtime) # last modified time (into a nice format)
    }


metadata = get_file_metadata(test_file)
print(metadata)

#############

#func, saves metadata to JSON
def save_to_JSON(data, filename="metadata.json"):
    with open(filename, "w") as file: #open file (write mode)
        json.dump(data, file, indent=4) #write to json (w/ nice indentation)


def scan_dir_and_store_metadata(directory):
    #list of file metadata to feed save_to_json func l8er
    file_metadata = [] 
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root,file)
            #add metadata of file to list
            file_metadata.append(get_file_metadata(file_path)) 
    save_to_JSON(file_metadata)

scan_dir_and_store_metadata(test_dir)

#############

#func, search metadata by keyword in file name
def search_metadata(data, search_term):
    #results = files where "name" contains the search_term (not case sensitive)
    results = [file for file in data if search_term.lower() in file['name'].lower()]
    return results
