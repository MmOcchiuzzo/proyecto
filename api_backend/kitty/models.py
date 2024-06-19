from django.db import models

# Create your models here.
class Kitty(models.Model):
    name = models.CharField(max_length=128)
    breed = models.CharField(max_length=128)
    fur = models.CharField(max_length=128)
    color = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.number} - {self.name}'


class User(models.Model):
    name = models.CharField(max_length=128)
    kitties = models.ManyToManyField(Kitty, blank=True)

    def __str__(self):
        return self.name