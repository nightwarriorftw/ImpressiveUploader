
# Handles upload, so your memory doesn't overwhelms
def handle_upload(file):
    with open('uploaded_file.csv', 'wb') as fileDestination:
        for chunks in file.chunks():
            fileDestination.write(chunks)
