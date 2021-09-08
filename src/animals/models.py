from django.db import models


class Specie(models.Model):
    name = models.CharField(max_length=50)
    proven_veracity = models.BooleanField(default=False)
