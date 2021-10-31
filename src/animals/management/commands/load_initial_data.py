from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from animals.models import Breed, Pet, Specie


class Command(BaseCommand):
    help = "Registra os dados iniciais da aplicação no banco de dados"

    def handle(self, *args, **options):

        specie_data = [
            {
                "model": "animals.specie",
                "fields": {"name": "cachorro", "proven_veracity": True},
            },
            {
                "model": "animals.specie",
                "fields": {"name": "gato", "proven_veracity": True},
            },
            {
                "model": "animals.specie",
                "fields": {"name": "roedor", "proven_veracity": True},
            },
            {
                "model": "animals.specie",
                "fields": {"name": "user-strange-specie-1", "proven_veracity": False},
            },
            {
                "model": "animals.specie",
                "fields": {"name": "user-strange-specie-2", "proven_veracity": False},
            },
        ]

        for data in specie_data:
            Specie.objects.get_or_create(
                name=data.get("fields").get("name"),
                proven_veracity=data.get("fields").get("proven_veracity"),
            )

        breed_data = [
            {
                "model": "animals.breed",
                "fields": {
                    "name": "pastor alemão",
                    "specie": Specie.objects.get(name="cachorro").pk,
                    "proven_veracity": True,
                },
            },
            {
                "model": "animals.breed",
                "fields": {
                    "name": "poodle",
                    "specie": Specie.objects.get(name="cachorro").pk,
                    "proven_veracity": True,
                },
            },
            {
                "model": "animals.breed",
                "fields": {
                    "name": "chihuahua",
                    "specie": Specie.objects.get(name="cachorro").pk,
                    "proven_veracity": True,
                },
            },
            {
                "model": "animals.breed",
                "fields": {
                    "name": "bulldog inglês",
                    "specie": Specie.objects.get(name="cachorro").pk,
                    "proven_veracity": True,
                },
            },
            {
                "model": "animals.breed",
                "fields": {
                    "name": "golden retriever",
                    "specie": Specie.objects.get(name="cachorro").pk,
                    "proven_veracity": True,
                },
            },
            {
                "model": "animals.breed",
                "fields": {
                    "name": "pug",
                    "specie": Specie.objects.get(name="cachorro").pk,
                    "proven_veracity": True,
                },
            },
            {
                "model": "animals.breed",
                "fields": {
                    "name": "persa",
                    "specie": Specie.objects.get(name="gato").pk,
                    "proven_veracity": True,
                },
            },
            {
                "model": "animals.breed",
                "fields": {
                    "name": "siamês",
                    "specie": Specie.objects.get(name="gato").pk,
                    "proven_veracity": True,
                },
            },
            {
                "model": "animals.breed",
                "fields": {
                    "name": "sphynx",
                    "specie": Specie.objects.get(name="gato").pk,
                    "proven_veracity": True,
                },
            },
            {
                "model": "animals.breed",
                "fields": {
                    "name": "coelho rex",
                    "specie": Specie.objects.get(name="roedor").pk,
                    "proven_veracity": True,
                },
            },
            {
                "model": "animals.breed",
                "fields": {
                    "name": "chinchila",
                    "specie": Specie.objects.get(name="roedor").pk,
                    "proven_veracity": True,
                },
            },
            {
                "model": "animals.breed",
                "fields": {
                    "name": "porquinho-da-índia",
                    "specie": Specie.objects.get(name="roedor").pk,
                    "proven_veracity": True,
                },
            },
            {
                "model": "animals.breed",
                "fields": {
                    "name": "hamster",
                    "specie": Specie.objects.get(name="roedor").pk,
                    "proven_veracity": True,
                },
            },
            {
                "model": "animals.breed",
                "fields": {
                    "name": "teddy",
                    "specie": Specie.objects.get(name="roedor").pk,
                    "proven_veracity": True,
                },
            },
            {
                "model": "animals.breed",
                "fields": {
                    "name": "abissínio",
                    "specie": Specie.objects.get(name="gato").pk,
                    "proven_veracity": True,
                },
            },
            {
                "model": "animals.breed",
                "fields": {
                    "name": "user-strange-breed-1",
                    "specie": Specie.objects.get(name="user-strange-specie-1").pk,
                    "proven_veracity": False,
                },
            },
            {
                "model": "animals.breed",
                "fields": {
                    "name": "user-strange-breed-2",
                    "specie": Specie.objects.get(name="user-strange-specie-1").pk,
                    "proven_veracity": False,
                },
            },
            {
                "model": "animals.breed",
                "fields": {
                    "name": "user-strange-breed-3",
                    "specie": Specie.objects.get(name="user-strange-specie-2").pk,
                    "proven_veracity": False,
                },
            },
            {
                "model": "animals.breed",
                "fields": {
                    "name": "user-strange-breed-4",
                    "specie": Specie.objects.get(name="user-strange-specie-2").pk,
                    "proven_veracity": False,
                },
            },
        ]

        for data in breed_data:
            Breed.objects.get_or_create(
                name=data.get("fields").get("name"),
                proven_veracity=data.get("fields").get("proven_veracity"),
                specie_id=data.get("fields").get("specie"),
            )

        user_data = [
            {
                "model": "auth.user",
                "fields": {
                    "password": "UnbFGA123",
                    "is_superuser": False,
                    "username": "joão",
                    "first_name": "",
                    "last_name": "",
                    "email": "joao@gmail.com",
                    "is_staff": False,
                },
            },
            {
                "model": "auth.user",
                "fields": {
                    "password": "UnbFGA123",
                    "is_superuser": False,
                    "username": "maria",
                    "first_name": "",
                    "last_name": "",
                    "email": "maria@gmail.com",
                    "is_staff": False,
                },
            },
            {
                "model": "auth.user",
                "fields": {
                    "password": "UnbFGA123",
                    "is_superuser": False,
                    "username": "pedro",
                    "first_name": "",
                    "last_name": "",
                    "email": "pedro@gmail.com",
                    "is_staff": False,
                },
            },
            {
                "model": "auth.user",
                "fields": {
                    "password": "UnbFGA123",
                    "is_superuser": False,
                    "username": "jorge",
                    "first_name": "",
                    "last_name": "",
                    "email": "jorge@gmail.com",
                    "is_staff": False,
                },
            },
            {
                "model": "auth.user",
                "fields": {
                    "password": "UnbFGA123",
                    "is_superuser": False,
                    "username": "antonio",
                    "first_name": "",
                    "last_name": "",
                    "email": "antonio@gmail.com",
                    "is_staff": False,
                },
            },
            {
                "model": "auth.user",
                "fields": {
                    "password": "UnbFGA123",
                    "username": "jojo",
                    "first_name": "",
                    "last_name": "",
                    "email": "jojo@gmai.com",
                    "is_staff": False,
                },
            },
        ]

        User = get_user_model()

        try:
            User.objects.create_superuser(
                username="admin",
                email="admin@admin.com",
                password="admin",
            )
        except IntegrityError as err:
            pass

        for data in user_data:
            user, created = User.objects.get_or_create(
                username=data.get("fields").get("username"),
                first_name=data.get("fields").get("first_name"),
                last_name=data.get("fields").get("last_name"),
                email=data.get("fields").get("email"),
                is_staff=data.get("fields").get("is_staff"),
            )
            user.set_password(data.get("fields").get("password"))
            user.save()

        pets_data = [
            {
                "model": "animals.pet",
                "fields": {
                    "name": "T-Rex",
                    "sex": "M",
                    "breed": Breed.objects.get(name="pastor alemão").pk,
                    "owner": User.objects.get(username="joão").pk,
                    "birth_date": "2021-09-01",
                    "is_neutered": False,
                    "color": "Preto",
                },
            },
            {
                "model": "animals.pet",
                "fields": {
                    "name": "Uncle Bob",
                    "sex": "M",
                    "breed": Breed.objects.get(name="user-strange-breed-4").pk,
                    "owner": User.objects.get(username="joão").pk,
                    "birth_date": "2020-04-01",
                    "is_neutered": True,
                    "color": "Green",
                },
            },
            {
                "model": "animals.pet",
                "fields": {
                    "name": "Floquinha",
                    "sex": "F",
                    "breed": Breed.objects.get(name="poodle").pk,
                    "owner": User.objects.get(username="maria").pk,
                    "birth_date": "2021-06-01",
                    "is_neutered": True,
                    "color": "Branco",
                },
            },
            {
                "model": "animals.pet",
                "fields": {
                    "name": "Flinstone",
                    "sex": "M",
                    "breed": Breed.objects.get(name="abissínio").pk,
                    "owner": User.objects.get(username="maria").pk,
                    "birth_date": "2003-02-08",
                    "is_neutered": True,
                    "color": "Branco",
                },
            },
            {
                "model": "animals.pet",
                "fields": {
                    "name": "Tigrão",
                    "sex": "F",
                    "breed": Breed.objects.get(name="chihuahua").pk,
                    "owner": User.objects.get(username="pedro").pk,
                    "birth_date": "2021-09-09",
                    "is_neutered": False,
                    "color": "caramelo",
                },
            },
            {
                "model": "animals.pet",
                "fields": {
                    "name": "Rainbow",
                    "sex": "F",
                    "breed": Breed.objects.get(name="teddy").pk,
                    "owner": User.objects.get(username="pedro").pk,
                    "birth_date": "2019-03-03",
                    "is_neutered": False,
                    "color": "caramelo",
                },
            },
            {
                "model": "animals.pet",
                "fields": {
                    "name": "cofen",
                    "sex": "F",
                    "breed": Breed.objects.get(name="persa").pk,
                    "owner": User.objects.get(username="jorge").pk,
                    "birth_date": "2021-06-15",
                    "is_neutered": False,
                    "color": "cinza",
                },
            },
            {
                "model": "animals.pet",
                "fields": {
                    "name": "mumu",
                    "sex": "M",
                    "breed": Breed.objects.get(name="teddy").pk,
                    "owner": User.objects.get(username="antonio").pk,
                    "birth_date": "2021-06-14",
                    "is_neutered": False,
                    "color": "cinza e branco",
                },
            },
            {
                "model": "animals.pet",
                "fields": {
                    "name": "garfield",
                    "sex": "M",
                    "breed": Breed.objects.get(name="user-strange-breed-1").pk,
                    "owner": User.objects.get(username="jojo").pk,
                    "birth_date": "2021-07-14",
                    "is_neutered": True,
                    "color": "laranja",
                },
            },
        ]

        for data in pets_data:
            Pet.objects.get_or_create(
                name=data.get("fields").get("name"),
                sex=data.get("fields").get("sex"),
                breed_id=data.get("fields").get("breed"),
                owner_id=data.get("fields").get("owner"),
                birth_date=data.get("fields").get("birth_date"),
                is_neutered=data.get("fields").get("is_neutered"),
                color=data.get("fields").get("color"),
            )

        self.stdout.write(
            self.style.SUCCESS("The database was successfully populated!")
        )
