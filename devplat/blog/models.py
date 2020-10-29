from django.db import models

class Event(models.Model):
    image = models.ImageField(upload_to='events-pics')
    title = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=False)
    facilitator = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class Home_Updates(models.Model):
    image = models.ImageField(upload_to='events-pics')
    title = models.CharField(max_length=200)
    quiz = models.CharField(max_length=500)
    content = models.TextField()
    def __str__(self):
        return self.title
