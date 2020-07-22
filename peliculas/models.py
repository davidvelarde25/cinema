from django.db import models

# Create your models here.

class Usuario(models.Model):
    uername = models.CharField(max_length=250, null=False)
    password = models.CharField(max_length=600, null=False)
    email = models.EmailField(max_length =254, null= False)
    name = models.CharField(max_length=600, null=False)
