from django.db import models

class members(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length = 100)
# Create your models here.
