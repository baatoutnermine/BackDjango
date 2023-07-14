import os
from django.db import models
import datetime as dt
from django.contrib.auth.models import User

from categorie.models import Categorie
# Create your models here.


CATEGORY_CHOICES = (
    ('fleurs','FLEURS'),
    ('voiture','VOITURE'),
    ('plage','PLAGE'),
    
   )

def filepath(request, filename):
    old_filename = filename
    timeNow = dt.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)
class Image(models.Model):   
     user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
     title= models.CharField(max_length=255 ,blank=True, null=True , default=None)      
     description= models.CharField(max_length=255 ,blank=True, null=True, default=None)
     image = models.ImageField(max_length=250,blank=True  ,default=None) 
     tags=models.CharField(max_length=200,null=True,choices=CATEGORY_CHOICES)
     categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True, default=None)