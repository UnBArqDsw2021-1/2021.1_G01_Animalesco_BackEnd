from django.db import models

from animals.models import Pet


class Bath(models.Model):

    bath_date = models.DateField(
        verbose_name="Bath date",
        null=False,
        blank=False,
    )

    next_bath_date = models.DateField(
        verbose_name="Next bath date",
        null=True,
        blank=True,
    )

    location_bath = models.CharField(
        verbose_name="Location bath",
        max_length=100,
        null=False,
        blank=False,
    )

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name="baths",
    )

    class Meta:
        unique_together = (
            "bath_date",
            "next_bath_date",
            "pet",
        )
