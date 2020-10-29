from django.db import models

from django.db import models

class Video(models.Model):
    name= models.CharField(max_length=500)
    videourl=models.CharField(max_length=2083)
    videscription = models.CharField(max_length=700)
    image = models.ImageField(upload_to='picha')

    def __str__(self):
        return self.name + ": " + str(self.videourl)

class Link(models.Model):
    link = models.CharField(max_length=200)  
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.link      