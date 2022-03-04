import os
from azure.storage.blob import BlobClient

import psycopg2

SUBSCRIPTION_ID = os.environ.get("SUBSCRIPTION_ID", None)

def uploadfile(BLOB_CONTAINER,blobname,cstr,filename):
    blob = BlobClient.from_connection_string(conn_str=cstr, container_name=BLOB_CONTAINER, blob_name=blobname)

    with open(filename, "rb") as data:
        blob.upload_blob(data)
    print("Uploaded file: {}\n To blob container {}".format(filename,BLOB_CONTAINER))

def appendDB(localfilename,container,blob,URL,cursor):
    SQL = "INSERT INTO blob1 (localfilename, BLOB_CONTAINER, blob_name, containerURL) VALUES (%s,%s,%s,%s);"
    data = (localfilename,container,blob,URL)
    cursor.execute(SQL,data)

def upload_appendDB():
    uploadfile(BLOB_CONTAINER,blob_name,cstr,localfilename)

    con = None
    try:
        con = psycopg2.connect("dbname={} user=postgres password = {}".format(localdbname,pw))
        cursor = con.cursor()

        appendDB(localfilename,BLOB_CONTAINER,blob_name,containerURL,cursor)

        con.commit()
        cursor.close()
        con.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()


if __name__ == '__main__':

    with open("./ignore.txt", 'r') as file:
        lines = [line.rstrip() for line in file]
    cstr = lines[0]
    pw = lines[1]

    storage_name = "mikestorageacademy"
    BLOB_CONTAINER = "mikecontainer"
    blob_name = "picture.png"
    localfilename = "./src/picture.png"
    containerURL = "https://"+storage_name+".blob.core.windows.net/"+BLOB_CONTAINER

    localdbname = "blobdb"
    
    #upload_appendDB()