from django.db import models

# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=255)
    join_date = models.DateField(null=True)


