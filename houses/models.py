from django.db import models


class House(models.Model):

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(
        verbose_name="Price", help_text="Posetive Numbers Only"
    )
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True)

    def __str__(self):
        return self.name
