from django.db import models


# Create your models here.
class Auth(models.Model):
    username = models.CharField(max_length=20)
    password = models.TextField(max_length=20)
    email_address = models.TextField(max_length=30)
    pat_token = models.TextField()
