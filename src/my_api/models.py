from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    vehicle = models.Charfield(max_length=64)
    human = models.Booleanfield()
    def __str__(self):
        return self.name