# << GOALS >>
# Traverse a directory
# For each file, collect & store metadata 
# Add search functionality

import os #for file navigation
import time #for last modified

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