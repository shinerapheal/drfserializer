from django.db import models

class people(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    location=models.CharField(max_length=100)
    adress=models.TextField() 
