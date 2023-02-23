import os
import zipfile

# Set your custom extension name here

custom_extension = ".j69"

def extract_custom_zip_files(folder_path):
    """
    Extract all zip files with custom extension from a folder.
    """
    for filename in os.listdir(folder_path):
        if filename.endswith(custom_extension):
            file_path = os.path.join(folder_path, filename)
            with zipfile.ZipFile(file_path, "r") as zip_ref:
                zip_ref.extractall(folder_path)

def compress_custom_zip_files(folder_path):
    """
    Compress all folders in a folder into zip files with custom extension.
    """
    for foldername in os.listdir(folder_path):
        folder_pathname = os.path.join(folder_path, foldername)
        if os.path.isdir(folder_pathname):
            zip_filename = foldername + custom_extension
            zip_filepath = os.path.join(folder_path, zip_filename)
            with zipfile.ZipFile(zip_filepath, "w", zipfile.ZIP_DEFLATED) as zip_ref:
                for root, dirs, files in os.walk(folder_pathname):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zip_ref.write(file_path, os.path.relpath(file_path, folder_pathname))


folder_path = "/path/to/folder"

extract_custom_zip_files(folder_path)


compress_custom_zip_files(folder_path)
