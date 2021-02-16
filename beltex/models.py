from django.db import models


class Production (models.Model):
    specialist = models.CharField(max_length=100)
    object = models.CharField(max_length=100)
    term = models.IntegerField(default=0)
    price = models.IntegerField(default=0)


class Specialists (models.Model):
    specialist = models.CharField(max_length=100)
    skills = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    car = models.CharField(max_length=1)
    photo = models.ImageField()

class Archive (models.Model):
    object = models.CharField(max_length=100)
    specialist = models.CharField(max_length=100)
    date = models.IntegerField(default=0)




