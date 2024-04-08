from django.db import models
import datetime
import os


def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class Category(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text='0-show,1-hidden')
    created_at=models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.name

class Musics(models.Model):
    category  =models.ForeignKey(Category,on_delete=models.CASCADE)              
    name=models.CharField(max_length=150,null=False,blank=False)
    owner=models.CharField(max_length=150,null=False,blank=False)
    music_image=models.ImageField(upload_to=getFileName,null=False,blank=False)
    audio=models.FileField(upload_to='audio/',null=False,blank=False)
    rate=models.FloatField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text='0-show,1-hidden')
    trending=models.BooleanField(default=False,help_text='0-default,1-trending')
    created_at=models.DateTimeField(auto_now_add=True)

    