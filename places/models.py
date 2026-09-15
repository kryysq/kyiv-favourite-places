from django.db import models
from django.contrib.auth.models import User


class Place(models.Model):
    PLACE_TYPES = [
        ('restaurant', 'Ресторан'),
        ('cafe', 'Кафе'),
        ('park', 'Парк'),
        ('entertainment', 'Розваги'),
        ('other', 'Інше'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    place_type = models.CharField(
        max_length=20,
        choices=PLACE_TYPES
    )
    address = models.CharField(
        max_length=200,
        blank=True
    )
    rating = models.IntegerField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name