from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Animal(models.Model):
    # null -> None              # blank -> ""
    name = models.CharField(max_length=100, null=False, blank=False)
    birth_date = models.DateField()
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    tricks = models.IntegerField(default=0)

    def __str__(self):
        return f"<name={self.name}>"

# Animal.objects.create(name="Alex", birth_date="2020-01-01", weight_kg=12.5, tricks=2, owner)