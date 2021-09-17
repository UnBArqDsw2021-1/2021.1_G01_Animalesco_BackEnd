from django.db import models
from animals.models import Pet

class Medicine(models.Model):
    name = models.CharField(
        verbose_name="Medicine name",
        max_length=100,
        null=False,
        blank=False,
    )

    start_date = models.DateField(
        verbose_name="Start date",
        null=False,
        blank=False,
    )

    finish_date = models.DateField(
        verbose_name="Finish date",
        null=True,
        blank=True,
    )

    aplication_time = models.TimeField(
        verbose_name="Aplication time",
        null=True,
        blank=True,
    )

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name="medicine",
    )

    class Meta:
        unique_together = ('name', 'pet',)

    def __str__(self) -> str:
        return self.name

