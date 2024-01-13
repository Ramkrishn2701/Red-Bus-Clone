from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Journey(models.Model):
    
    from_location=models.CharField(max_length=30)
    to_location=models.CharField(max_length=30)
    date=models.DateField(auto_now_add=False)

class Travels(models.Model):
    journey_pk=models.CharField(max_length=30,primary_key=True)
    travels=models.CharField(max_length=1000, blank=True, null=True)
    def set_travels(self, value):
        self.travels= value
