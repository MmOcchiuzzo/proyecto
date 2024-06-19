from django.db import models

# Create your models here.

class Puppy(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=100)
    vaccinated = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=128)
    puppies = models.ManyToManyField(Puppy, blank=True)

    def __str__(self):
        return self.name