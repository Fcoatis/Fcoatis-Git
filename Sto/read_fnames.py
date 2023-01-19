from google.cloud import storage

def list_files():
    storage_client = storage.Client()
    blobs = storage_client.list_blobs('coatis') 
    for blob in blobs:
        print(blob.name)
    return       