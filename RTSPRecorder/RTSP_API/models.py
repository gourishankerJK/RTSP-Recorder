from django.db import models
from django.utils import timezone

# Create your models here.
class Camera(models.Model):
    name = models.CharField(max_length=50,unique = True)
    url = models.CharField(max_length=150)
    status = models.BooleanField(default=False)
    active_hours = models.CharField(max_length=50)
    def __str__(self):
    	return self.name

class Recording(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=150)
    status = models.BooleanField(default = True)
    recorded_time = models.DateTimeField(default = timezone.now)
    camera = models.ForeignKey(Camera,on_delete = models.SET_NULL,null = True)
