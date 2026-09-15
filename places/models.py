from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    rating = models.IntegerField()

    def __str__(self):
        return self.name