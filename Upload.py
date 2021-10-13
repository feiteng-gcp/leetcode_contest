import os, requests, json, pathlib, subprocess, pytz, time, stat, collections
from datetime import datetime
import logging, IO_Helper, traceback
import logging.config
import Logger, concurrent.futures
from os import path
from multiprocessing import Manager

from google.cloud import storage
import sys, hashlib

def file_hashcode(file_name):
    md5 = hashlib.md5()
    with open(file_name, 'r') as f:
        while True:
            data = f.read(hmd5.block_size)
            if not data: break
            md5.update(data)
    return md5.hexdigest()

def upload_blob(source_file_name, destination_blob_name, logger, submit_dict):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    #######################################
    source_file_content_hash = 
    if source_file_name in submit_dict:
        print('Already uploaded file {}'.format(source_file_name))
        return
    try:        
        bucket_name = "jplagresult"
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        # print("File {} uploaded to {}.".format(source_file_name, destination_blob_name))
        print("Uploaded file {} to Google CLoud Storage.".format(source_file_name))
        #######################################

        submit_dict[source_file_name] = '1'
        return True
    except Exception as err:
        traceback.print_exc()
        print('Error when uploading file={}'.format(source_file_name))
    return False
    


def upload(logger):
    file_name = 'Upload_Record/To_Upload.json'
    # upload_blob(file_path, file_path, logger)
    file_content = IO_Helper.loadJSON(file_name)
    flag = True
    for key in file_content:
        # flag |= uploadFolder(key, logger)
        print(key)
    if flag: IO_Helper.writeJSON(file_name, '[]')

def uploadFolder(contest_title_slug, logger):
    folder_name = 'JPLAGResult/' + contest_title_slug
    submit_dict = Manager().dict()
    upload_record_filname = 'Upload_Record/{}.json'.format(contest_title_slug)
    # print(upload_record_filname)
    submit_dict.update(IO_Helper.loadJSON(upload_record_filname))
    flag = True
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for path, subdirs, files in os.walk(folder_name):
            for name in files:
                filePath = os.path.join(path, name)
                filename = filePath.replace("\\", "/")
                task = executor.submit(upload_blob, filename, filename, logger, submit_dict)
                flag |= task.result()
    IO_Helper.writeJSON(upload_record_filname, submit_dict.copy())
    return flag
    


def test_upload():
    targ_file = 'test/test_folders/upload_test_file'
    uploadFile(targ_file)
    
if __name__ == '__main__':
    uploadFolder('test/uploadFolder_test')
