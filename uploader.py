import dropbox

SECRET_KEY_FOR_API = 'KEY OF API DROPBOX V2: https://www.dropbox.com/developers '

class TransferData:
    def __init__(self):
        self.access_token = SECRET_KEY_FOR_API
        self.dbx = dropbox.Dropbox(self.access_token)

    def upload_file(self, arq, remoto):
        self.dbx.files_upload(arq, remoto)
        meta = self.dbx.sharing_create_shared_link(remoto)
        url = meta.url
        url = url.replace('?dl=0', '?dl=1')
        return url

'''
USAGE

It works with all of image types. I do not test it with videos.
Sorry my bad english.

In your views.py or other file:

from uploader import *

#Create TransferData object
dbx = TransferData()

#Open the archive
arq = open('file.jpg', 'rb')

#upload the file
url = dbx.upload_file(arq, '/file.jpg' )


The URL returned by this is usable in "<img src="url">".
'''

