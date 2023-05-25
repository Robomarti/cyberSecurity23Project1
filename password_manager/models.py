from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ListablePassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=30)
    web_address = models.CharField(max_length=200)

    def __str__(self):
        return self.password
