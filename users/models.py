from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")
        OTHER = ("other", "Other")

    class LanguageChocies(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "Engilsh")
        JP = ("jp", "Japanese")
        CH = ("ch", "Chinese")
        RU = ("ru", "Russian")
        FR = ("fr", "French")

    class CurrencyChocies(models.TextChoices):
        WON = "won", "Korean Won"
        USD = "usd", "Dollar"
        JPY = "jpy", "Japan Yen"
        CNY = "cny", "China	Renminbi"
        RUB = "rub", "Russian Ruble"
        EUR = "eur", "Euro"

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    name = models.CharField(
        max_length=150,
        default="null",
    )

    photo = models.ImageField()

    is_host = models.BooleanField(default=False)

    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )

    language = models.CharField(
        max_length=2,
        choices=LanguageChocies.choices,
    )

    currency = models.CharField(
        max_length=10,
        choices=CurrencyChocies.choices,
    )
