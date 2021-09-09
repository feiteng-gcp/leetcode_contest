from google.cloud import storage
import os
from os import listdir
from os.path import isfile, join
import glob


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    # print("Uploading to Google Cloud Storage..." + source_file_name)
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)



def uploadFolder(folderName):
    bucket_name = 'jplagresult'
    print("Uploading to Google Cloud Storage.." + folderName)
    for path, subdirs, files in os.walk(folderName):
        for name in files:
            filePath = os.path.join(path, name)
            filePath = filePath.replace("\\", "/")
            # this will overwrite file with same name
            upload_blob(bucket_name, filePath, filePath)



