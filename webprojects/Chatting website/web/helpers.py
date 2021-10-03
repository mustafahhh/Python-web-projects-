import os
import uuid
from django.core.files.base import ContentFile
from django.db.models.expressions import F
from django.utils.deconstruct import deconstructible
from PIL import Image, ImageOps
import io 
from io import BytesIO
import base64
from . import models


Mask = 'C:\\Users\\TM\\سطح المكتب\\New Folder\\web\\mask.png'


#for pfp images storing
@deconstructible
class RandomFileName(object):
    def __init__(self, path):
        self.path = os.path.join(path, "%s%s")

    def __call__(self, _, filename):
        # @note It's up to the validators to check if it's the correct file type in name or if one even exist.
        extension = os.path.splitext(filename)[1]
        return self.path % (uuid.uuid4(), extension)


def BasicToken():
    return 'BasicToken-' + str(uuid.uuid4()) +  str(uuid.uuid4()) 

def TokenToUser(token):
    try:
        return models.accounts.objects.get(token=token).user
    except Exception as ex:
        return 'None'


def roomcheck(room):

    return models.rooms.objects.filter(roomid=room).exists()

def TokenChecker(Token):
    return models.accounts.objects.filter(token=Token).exists()

def UserToImage(User):
    return models.accounts.objects.get(user=User).image

def dupechecker(Room,Token):
    try:
        usersconnected = models.rooms.objects.get(roomid=Room).usersconnected.split(',')
        print(usersconnected)
        for i in usersconnected:
            if i == Token:
                return 1
        
        return 0 
    except:
        print(Exception)
        return 1


def removeuser(Room,Token):
    try:
        usersconnectedlist = models.rooms.objects.get(roomid=Room).usersconnected
        if usersconnectedlist.startswith(Token):
            usersconnectedlist.replace(Token, '')+ ','

        else:
            usersconnectedlist.replace(Token+ ',','') 

        if usersconnectedlist.startswith(','):
            usersconnectedlist = usersconnectedlist[1:]
        if usersconnectedlist.isspace: 
            usersconnectedlist='None'




        print(usersconnectedlist + '\n')
        print(Room,Token,models.rooms.objects.get(roomid=Room).usersconnected)
        database = models.rooms.objects.get(roomid=Room)
        database.usersconnected = usersconnectedlist
        database.save()        
    except Exception as ex:
        print(ex)
        return

def adduser(Room,Token):
    try:
        if dupechecker(Room,Token) == 1:
            return
        else:

            usersconnectedlist = models.rooms.objects.get(roomid=Room).usersconnected
            if usersconnectedlist == '':
                newlist =  Token
            else: 
                newlist = usersconnectedlist + ',' + Token


            database = models.rooms.objects.get(roomid=Room)
            database.usersconnected = newlist
            database.save()
    except Exception as ex:
        print(ex)

        return

#for pfp resizing to circle
def RESIZE(Img):
    mask = Image.open(Mask).convert('L')
    im = Image.open(Img)
    outputimage = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
    outputimage.putalpha(mask)

    #Convering the image to django file so we can upload it to our database
    image_io = io.BytesIO()
    outputimage.save(image_io, format='png')
    outputimage = '{}.{}'.format('filename','.png')
    image = ContentFile(image_io.getvalue(), outputimage)
    return image


#This will return if the file is larger than the limit
def file_size(value,file_size_limit): # add this to some file where you can import it from
    limit = file_size_limit*1024*1024 #megabytes to bytes
    if value.size > limit:#the file is already bytes so we don't need to convert
        return 1
    return 0 
def decodebytes(bytes):
    return bytes.decode('utf-8').replace("'", '"')
