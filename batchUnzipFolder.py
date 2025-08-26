# unzip all .zip files in a specified directory into separate folders
# if a folder with the same name already exists, skip that file
# usage: change the zip_directory variable to your folder path
# optional: change output_directory to specify a different extraction location
# if output_directory is None, it will extract in the same directory as the zip files
# requires Python 3.x
# by Christine Anuli, 2024-06

import os
import zipfile

def batch_unzip(zip_dir, output_dir=None):
    if output_dir is None:
        output_dir = zip_dir  # extract into the same directory by default

    # make output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok = True)

    # Loop through all .zip files in the directory
    for filename in os.listdir(zip_dir):
        if filename.lower().endswith('.zip'): # check for .zip files
            zip_path = os.path.join(zip_dir, filename) # full path to the zip file
            extract_folder_name = os.path.splitext(filename)[0] # folder name without .zip
            extract_path = os.path.join(output_dir, extract_folder_name) # full path to extract folder

            if os.path.exists(extract_path):
                print(f"'{filename}' skipped! ('{filename}' was already extracted).")
                continue
            try:
                with zipfile.ZipFile(zip_path, 'r') as zip_ref: # open the zip file
                    zip_ref.extractall(extract_path) # extract to the folder
                    print(f"'{filename}' successfuly extracted  to '{extract_path}'") # success message
            except zipfile.BadZipFile: 
                print(f"ERROR: '{filename}' is not a valid zip file.") # error handling for invalid zip files
# Example usage
if __name__ == "__main__":
    zip_directory =  # Change this to your folder path
    batch_unzip(zip_directory,None)
