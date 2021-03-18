from django.db import models


class Employee(models.Model):

    name = models.CharField(max_length=100,blank= False)
    mobile = models.IntegerField(blank= False)
    location = models.CharField(max_length=100,blank= False)
    title = models.CharField(max_length=100,blank= False)
    department = models.CharField(max_length=100,blank= False)
    project = models.CharField(max_length=100,blank= False)
    email = models.CharField(max_length=100,blank= False)

 
