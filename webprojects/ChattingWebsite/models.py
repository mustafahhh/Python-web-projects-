from django.db import models
# Create your models here.
from .helpers import RandomFileName,BasicToken

class rooms(models.Model):
    roomid = models.CharField(max_length=6)
    usersconnected = models.TextField()



    def __str__(self):
        return f"{self.roomid}|"



class messages(models.Model):
    roomid = models.CharField(max_length=6)    
    message = models.TextField(blank=True,max_length=64)
    user = models.CharField(max_length=15)




class accounts(models.Model):
    user = models.CharField(max_length=15)
    image = models.ImageField(upload_to=RandomFileName('files'))
    mytoken = BasicToken()
    token = models.CharField(max_length=200,default=mytoken)

    def __str__(self):
        return f"{self.image}"