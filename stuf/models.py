import email
from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=70)
    password = models.CharField(max_length=70)
    cpassword = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
