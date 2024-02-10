from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 70)
    email = models.EmailField()
    password = models.CharField( max_length=100)
    retype_pass = models.CharField( max_length=100)