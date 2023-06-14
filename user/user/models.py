from django import models


class User(models.Model):
    username = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
