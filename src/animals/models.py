from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


# Django User Model
User = get_user_model()


class Specie(models.Model):
    name = models.CharField(verbose_name='specie name', max_length=50, unique=True)

    # O usuário pode criar novas espécies, mas enquanto a veracidade dessa espécie não
    # for comprovada, não irá aparecer para os demais usuários, somente para o criador.
    proven_veracity = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super().save(*args, **kwargs)


class Breed(models.Model):
    name = models.CharField(verbose_name='breed name', max_length=50)

    # related_name="breeds" é o nome que será usado para fazer as associações de
    # specie para breed. Por exemplo, usando o ORM do django, para pegar todas as raças de cachorros fariámos algo do tipo:
    # > Specie.objects.get(name="Cachorro").breeds.all()
    specie = models.ForeignKey(Specie, on_delete=models.PROTECT, related_name="breeds")

    # O usuário pode criar novas espécies, mas enquanto a veracidade dessa espécie não
    # for comprovada, não irá aparecer para os demais usuários, somente para o criador.
    proven_veracity = models.BooleanField(default=False)

    # A classe Meta são todas as metainformações da classe Breed
    class Meta:
        # unique_together é uma meta informação que define chaves únicas compostas
        unique_together = ('name', 'specie',)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super().save(*args, **kwargs)


class Pet(models.Model):
    name = models.CharField(verbose_name='pet name', max_length=100)

    # A classe `SexOptions` é a maneira Django de criar enums
    class SexOptions(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')

    # sex é um charfield que possui um enum de opções, sendo MALE o valor padrão
    sex = models.CharField(
        max_length=1,
        choices=SexOptions.choices,
        default=SexOptions.MALE
    )

    breed = models.ForeignKey(Breed, on_delete=models.PROTECT)

    # Se o usuário deletar a conta, nos deletamos os pets cadastrados
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets')

    birth_date = models.DateField()

    is_neutered = models.BooleanField(default=False)

    color = models.CharField(max_length=100)

    # Em algum momento teremos que receber imagens, e isso é bem complicado de se fazer
    # picture = models.ImageField(upload_to='animals_pictures/', null=True, blank=True)

    # Método estático possui essa sintaxe
    # Ps.: Métodos estáticos são métodos que não dependem de instâncias, podem ser chamados diretamente da classe
    @staticmethod
    def get_valid_sex_options() -> str:
        """
        Retorna as opções válidas para o atributo sex da classe Pet

        Returns:
            str:
        """
        return ' | '.join(f'{abrv} for {desc}' for abrv, desc in Pet.SexOptions.choices )