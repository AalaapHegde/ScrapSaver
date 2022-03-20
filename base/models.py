from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    userName = models.CharField(max_length = 30)
    organizationName = models.CharField(max_length=200)
    password = models.CharField(max_length = 20)
    zipCode = models.IntegerField(default=0)



class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null= True, blank=True)
    title = models.CharField(max_length=200)
    quantity = models.IntegerField(default = 0)
    description = models.TextField( null= True, blank=True)
    created = models.DateTimeField('date created')

    def __str__(self):
        return self.title
    

