from django.db import models

# Create your models here.

class User(models.Model):
    username_text = models.CharField(max_length=30)

class Passwords(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    password_text = models.CharField(max_length=30)
