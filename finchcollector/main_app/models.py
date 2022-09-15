from django.db import models
from django.urls import reverse


# Create your models here.

class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
      return self.name

    def get_absolute_url(self):
            return reverse('finch_detail', kwargs={'finch_id': self.id})
