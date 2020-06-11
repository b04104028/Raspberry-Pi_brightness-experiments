from picamera import PiCamera
from time import sleep
import time
import os
import datetime
from google.cloud import storage

project_id = 'ChanLab'
bucket_name = 'chanlab-169504.appspot.com'
storage_client = storage.Client.from_service_account_json('ChanLab-7943087c5a6b.json')



def upload_blob(bucket_name, source_file_name, destination_blob_name):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name, content_type='image/jpg')
    blob.make_public()
    myurl=blob.public_url
    os.remove(source_file_name)
    return myurl


n = 0
while True:
    n = datetime.datetime.now()
    action="raspistill -t 3000 -o photo1001" +datetime.datetime.strftime(n,"%Y-%m-%d_%H%M")+ ".png -e png -w 640 -h 480"#
    os.system(action)
    #before uploading, analyze the photo or not??


    #upload
    datetime.datetime.strftime(n,"%Y-%m-%d_%H%M")
    destination_blob_name = "photo1001" + datetime.datetime.strftime(n,"%Y-%m-%d_%H%M") + ".png"
    source_file_name = os.getcwd()+'/'+ destination_blob_name
    myurl=upload_blob(bucket_name, source_file_name, destination_blob_name)
    #myurl=upload_blob(bucket_name, source_file_name, 'test.png')

    print(myurl)
    with open(r'/home/pi/Desktop/Pictures//' +'LEFT' + str(datetime.date.today())+'.txt','a',newline='') as f:
        f.write(myurl+'\n')


    time.sleep(300)
















#raspivid -w 800 -h 600 -fps 25 -b 1000000 -t 99999 -o /home/pi/Desktop/Pictures/bammmm.h264
#raspivid -vf -hf -f -t 0 -w 640 -h 360 -fps 30 -e h264 -o /home/Desktop/Pictures/bammm.h264




#from google.cloud import storage
#import io, os

'''project_id = 'CAMERA'
bucket_name = ''
destination_blob_name = 'images'
storage_client = storage.Client.from_service_account_json('')'''


'''def upload_blob(bucket_name, source_file_name, destination_blob_name):
    
    storage_client=storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    blob.make_public()
    myurl = blob.public_url
    os.remove'''
                              
                        
#camera = PiCamera()

#camera.start_preview()
#sleep(10)
#camera.stop_preview()
