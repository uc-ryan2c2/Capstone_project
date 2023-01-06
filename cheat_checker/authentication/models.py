from django.db import models


# Create your models here.
class Auth(models.Model):
    username = models.CharField(max_length=20, blank=False, null=False)
    password = models.CharField(max_length=150, blank=False, null=False)
    email_address = models.TextField(max_length=50, blank=False, null=False)
    canvas_token = models.TextField(blank=False, null=False)

    def __str__(self):
        # this will name the object entry within the database to the username that was entered
        return self.username
