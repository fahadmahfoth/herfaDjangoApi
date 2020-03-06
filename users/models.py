from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Jobs(models.Model):
    job        = models.CharField(max_length=200)
    def __str__(self):
        return self.job

class Users(models.Model):
    user        = models.ForeignKey(User,on_delete=models.CASCADE)
    fullName    = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=15)
    area        = models.CharField(max_length=200)
    job         = models.ForeignKey(Jobs,on_delete=models.CASCADE)
    date        = models.DateField(auto_now_add=True,auto_now=False)
    whatsApp    = models.BooleanField(default=False)
    


    def __str__(self):
        return self.user.username

    




    