# << GOALS >>
# Traverse a directory
# For each file, collect & store metadata 
# Add search functionality

import os #for file navigation
import time #for last modified
import json #for metadata storage

TEST_DIR = r"C:\Users\itspebbleboy\Documents\GitHub\File-Metadata-Search-Tool-Python\test_folder"
TEST_FILE = r"C:\Users\itspebbleboy\Documents\GitHub\File-Metadata-Search-Tool-Python\test_folder\file.txt"

DEFAULT_METADATA_FILE = "metadata.json"

#basic func: scans a directory & prints paths of all files
def scan_directory(directory):
    #walk thru directories & subdirectories
    for root, _, files in os.walk(directory):
        for file in files: #iter thru all files in curr dir
            file_path = os.path.join(root,file)

#func: gets metadata of file
def get_file_metadata(file_path):
    stats = os.stat(file_path) #get file stats
    return{
        "name": os.path.basename(file_path), #file name from path
        "size": stats.st_size, # file size (bytes)
        "type": os.path.splitext(file_path)[1], #file extension
        "last_modified": time.ctime(stats.st_mtime) # last modified time (into a nice format)
    }

#func: saves metadata to JSON
def save_to_JSON(data, filename = DEFAULT_METADATA_FILE):
    with open(filename, "w") as file: #open file (write mode)
        json.dump(data, file, indent=4) #write to json (w/ nice indentation)

#func: scans dir, stores files' metadata into the output file
def scan_dir_and_store_metadata(directory, output_file = DEFAULT_METADATA_FILE):
    #list of file metadata to feed save_to_json func l8er
    file_metadata = [] 
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root,file)
            #add metadata of file to list
            file_metadata.append(get_file_metadata(file_path)) 
    save_to_JSON(file_metadata, output_file)

#func: search metadata by keyword in file name
def search_metadata(data, search_term):
    #results = files where "name" contains the search_term (not case sensitive)
   return [file for file in data if search_term.lower() in file['name'].lower()]


if __name__ == "__main__":
    #scan directory & save metadata to default JSON file
    scan_dir_and_store_metadata(TEST_DIR)
    #load that file
    with open(DEFAULT_METADATA_FILE, "r") as file:
        metadata_list = json.load(file) #load json as py list

    search_results = search_metadata(metadata_list, "1")
    print(search_results)

