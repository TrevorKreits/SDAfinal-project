from django.db import models
from django.contrib.auth.models import User

class Services(models.Model):
    service = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.service

class Providers(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Profile(models.Model):
    country = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    date_birth = models.DateField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username