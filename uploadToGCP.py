from google.cloud import storage
import os, Logger, pytz
from os import listdir
from os.path import isfile, join
import glob
from datetime import datetime


def upload_blob(bucket_name, source_file_name, 
    destination_blob_name, logger):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    curTime = datetime.now(pytz.timezone('America/New_York'))
    cur_time = curTime.strftime('%Y %b %d %H:%M %p %z')
    logger.info("[%s] filename=%s is uploaded to Google Cloud Storage..." % (cur_time, source_file_name))


def uploadFolder(folderName):
    bucket_name = 'jplagresult'
    logger = Logger.getLogger("GCP_Upload")
    for path, subdirs, files in os.walk(folderName):
        for name in files:
            filePath = os.path.join(path, name)
            filename = filePath.replace("\\", "/")
            # this will overwrite file with same name
            upload_blob(bucket_name, filename, filename, logger)

def uploadFile(filename):
    bucket_name = 'jplagresult'
    logger = Logger.getLogger("GCP_Upload")
    upload_blob(bucket_name, filename, filename, logger)
