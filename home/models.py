from django.db import models

# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=255)
    join_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=200)
    date = models.DateField(max_length=200)
    contents = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}"