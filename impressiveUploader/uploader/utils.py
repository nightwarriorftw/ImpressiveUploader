import os
from impressiveUploader.settings import MEDIA_ROOT

''' 
    Handles upload, so your memory doesn't overwhelms
    by breaking them into chunks.
'''
def handle_upload(file):
    saved_location = os.path.join(MEDIA_ROOT)
    fileName = file.name
    with open(os.path.join(saved_location,fileName), 'wb') as fileDestination:
        for chunks in file.chunks():
            print("Writing chunk")
            fileDestination.write(chunks)
