from django.db import models

# Create your models here.
class IotChannelData(models.Model):
    name = models.CharField(max_length=200) 
    value = models.CharField(max_length=200) 


    def __str__(self):
        return self.name


class Esp32camImg(models.Model):
    UpdatingImg =  models.ImageField(upload_to='media/images',default='esp32-cam.jpg', blank=True,null = True)
    def __str__(self):
        return self.UpdatingImg