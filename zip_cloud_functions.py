'''
A module to prepare all the cloud functions for a Terraform deployment in GCP.
'''

import os
import zipfile

def zip_directory(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, mode='w', compression=zipfile.ZIP_DEFLATED) as zipf:
        len_dir_path = len(folder_path)
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, file_path[len_dir_path:])

if __name__ == '__main__':
    directory = "cloud_functions"
    for cloud_function in os.listdir(directory):
        if os.path.isdir(f"{directory}/{cloud_function}"):
            zip_directory(f"{directory}/{cloud_function}", f"{cloud_function}.zip")
