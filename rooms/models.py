from django.db import models

# Create your models here.


class Room(models.Model):
    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Privateroom")
        SHARED_ROOM = ("shared_room", "Shared Room")

    country = models.CharField(
        max_length=50,
        default="한국",
    )

    city = models.CharField(
        max_length=80,
        default="서울",
    )

    address = models.CharField(
        max_length=250,
    )

    price = models.PositiveIntegerField()

    rooms = models.PositiveIntegerField()

    toilets = models.PositiveIntegerField()

    pet_friendly = models.BooleanField(
        default=True,
    )

    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )

    description = models.TextField()


class Amenity(models.Model):

    """Amenity Definition"""

    name = models.CharField(
        max_length=150,
    )

    description = models.CharField(
        max_length=150,
        null=True,
    )
