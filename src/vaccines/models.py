from django.db import models
from animals.models import Pet

class Vaccine(models.Model):
    name = models.CharField(verbose_name="Vaccine name", max_length=100, null=False, blank=False)
    application_date = models.DateField(verbose_name="Dose application date", null=False, blank=False)
    next_application_date = models.DateField(verbose_name="Next dose application date")
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    # Para que seja possível realizar um melhor controle gráfico das vacinas, este campo booleano informa se a vacina terá ou não
    # próxima dose. Em casos de vacinas de dose única ou vacinas que não precisarão ser tomadas novamente.
    is_finished = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name