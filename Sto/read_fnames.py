from google.cloud import storage

def list_files():
    storage_client = storage.Client()
    blobs = storage_client.list_blobs('sz-00003-ws/datalake/precos-mercado/B3/out') 
    for blob in blobs:
        print(blob.name)
    return       