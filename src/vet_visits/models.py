from django.db import models

from animals.models import Pet


class VetVisit(models.Model):
    vet_clinic = models.CharField(
        verbose_name="Veterinary clinic name",
        max_length=100,
        null=False,
        blank=False,
    )

    description = models.TextField(
        verbose_name="Description of the visit purpose",
        max_length=350,
        null=True,
        blank=True,
    )

    visit_date = models.DateField(
        verbose_name="Vet visit date",
        null=False,
        blank=False,
    )

    next_visit_date = models.DateField(
        verbose_name="Next vet visit date",
        null=True,
        blank=True,
    )

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name="vet_visits",
    )

    def __str__(self) -> str:
        return (
            str(self.pet)
            + " visited "
            + self.vet_clinic
            + " at day "
            + str(self.visit_date)
        )
