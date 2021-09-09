from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError


from animals.models import Specie, Breed, Pet


class Command(BaseCommand):
    help = 'Registra os dados iniciais da aplicação no banco de dados'

    def handle(self, *args, **options):

        specie_data  = [
            {
                "model": "animals.specie",
                "pk": 1,
                "fields": {
                    "name": "Cachorro",
                    "proven_veracity": True
                }
            },
            {
                "model": "animals.specie",
                "pk": 2,
                "fields": {
                    "name": "Gato",
                    "proven_veracity": True
                }
            },
            {
                "model": "animals.specie",
                "pk": 3,
                "fields": {
                    "name": "Roedor",
                    "proven_veracity": True
                }
            },
            {
                "model": "animals.specie",
                "pk": 4,
                "fields": {
                    "name": "user-strange-specie-1",
                    "proven_veracity": False
                }
            },
            {
                "model": "animals.specie",
                "pk": 5,
                "fields": {
                    "name": "user-strange-specie-2",
                    "proven_veracity": False
                }
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
                "pk": 1,
                "fields": {
                    "name": "Pastor Alemão",
                    "specie": 1,
                    "proven_veracity": True
                }
            },
            {
                "model": "animals.breed",
                "pk": 2,
                "fields": {
                    "name": "Poodle",
                    "specie": 1,
                    "proven_veracity": True
                }
            },
            {
                "model": "animals.breed",
                "pk": 3,
                "fields": {
                    "name": "Chihuahua",
                    "specie": 1,
                    "proven_veracity": True
                }
            },
            {
                "model": "animals.breed",
                "pk": 4,
                "fields": {
                    "name": "Persa",
                    "specie": 2,
                    "proven_veracity": True
                }
            },
            {
                "model": "animals.breed",
                "pk": 5,
                "fields": {
                    "name": "Siamês",
                    "specie": 2,
                    "proven_veracity": True
                }
            },
            {
                "model": "animals.breed",
                "pk": 6,
                "fields": {
                    "name": "Sphynx",
                    "specie": 2,
                    "proven_veracity": True
                }
            },
            {
                "model": "animals.breed",
                "pk": 7,
                "fields": {
                    "name": "Coelho Rex",
                    "specie": 3,
                    "proven_veracity": True
                }
            },
            {
                "model": "animals.breed",
                "pk": 8,
                "fields": {
                    "name": "Teddy",
                    "specie": 3,
                    "proven_veracity": True
                }
            },
            {
                "model": "animals.breed",
                "pk": 9,
                "fields": {
                    "name": "Abissínio",
                    "specie": 3,
                    "proven_veracity": True
                }
            },
            {
                "model": "animals.breed",
                "pk": 10,
                "fields": {
                    "name": "user-strange-breed-1",
                    "specie": 4,
                    "proven_veracity": False
                }
            },
            {
                "model": "animals.breed",
                "pk": 11,
                "fields": {
                    "name": "user-strange-breed-2",
                    "specie": 4,
                    "proven_veracity": False
                }
            },
            {
                "model": "animals.breed",
                "pk": 12,
                "fields": {
                    "name": "user-strange-breed-3",
                    "specie": 5,
                    "proven_veracity": False
                }
            },
            {
                "model": "animals.breed",
                "pk": 13,
                "fields": {
                    "name": "user-strange-breed-4",
                    "specie": 5,
                    "proven_veracity": False
                }
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
                "pk": 2,
                "fields": {
                    "password": "UnbFGA123",
                    "is_superuser": False,
                    "username": "joão",
                    "first_name": "",
                    "last_name": "",
                    "email": "joao@gmail.com",
                    "is_staff": False,
                }
            },
            {
                "model": "auth.user",
                "pk": 3,
                "fields": {
                    "password": "UnbFGA123",
                    "is_superuser": False,
                    "username": "maria",
                    "first_name": "",
                    "last_name": "",
                    "email": "maria@gmail.com",
                    "is_staff": False,
                }
            },
            {
                "model": "auth.user",
                "pk": 4,
                "fields": {
                    "password": "UnbFGA123",
                    "is_superuser": False,
                    "username": "pedro",
                    "first_name": "",
                    "last_name": "",
                    "email": "pedro@gmail.com",
                    "is_staff": False,
                }
            },
            {
                "model": "auth.user",
                "pk": 5,
                "fields": {
                    "password": "UnbFGA123",
                    "is_superuser": False,
                    "username": "jorge",
                    "first_name": "",
                    "last_name": "",
                    "email": "jorge@gmail.com",
                    "is_staff": False,
                }
            },
            {
                "model": "auth.user",
                "pk": 6,
                "fields": {
                    "password": "UnbFGA123",
                    "is_superuser": False,
                    "username": "antonio",
                    "first_name": "",
                    "last_name": "",
                    "email": "antonio@gmail.com",
                    "is_staff": False,
                }
            },
            {
                "model": "auth.user",
                "pk": 7,
                "fields": {
                    "password": "UnbFGA123",
                    "username": "jojo",
                    "first_name": "",
                    "last_name": "",
                    "email": "jojo@gmai.com",
                    "is_staff": False,
                }
            },
        ]

        User = get_user_model()

        try:
            User.objects.create_superuser(
                username='admin',
                email='admin@admin.com',
                password='admin',
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
                "pk": 1,
                "fields": {
                    "name": "T-Rex",
                    "sex": "M",
                    "breed": 1,
                    "owner": 2,
                    "birth_date": "2021-09-01",
                    "is_neutered": False,
                    "color": "Preto"
                }
            },
            {
                "model": "animals.pet",
                "pk": 2,
                "fields": {
                    "name": "Floquinha",
                    "sex": "F",
                    "breed": 2,
                    "owner": 3,
                    "birth_date": "2021-06-01",
                    "is_neutered": True,
                    "color": "Branco"
                }
            },
            {
                "model": "animals.pet",
                "pk": 3,
                "fields": {
                    "name": "Tigrão",
                    "sex": "F",
                    "breed": 3,
                    "owner": 4,
                    "birth_date": "2021-09-09",
                    "is_neutered": False,
                    "color": "caramelo"
                }
            },
            {
                "model": "animals.pet",
                "pk": 4,
                "fields": {
                    "name": "cofen",
                    "sex": "F",
                    "breed": 7,
                    "owner": 3,
                    "birth_date": "2021-06-15",
                    "is_neutered": False,
                    "color": "cinza"
                }
            },
            {
                "model": "animals.pet",
                "pk": 5,
                "fields": {
                    "name": "mumu",
                    "sex": "M",
                    "breed": 10,
                    "owner": 2,
                    "birth_date": "2021-06-14",
                    "is_neutered": False,
                    "color": "cinza e branco"
                }
            },
            {
                "model": "animals.pet",
                "pk": 6,
                "fields": {
                    "name": "garfield",
                    "sex": "M",
                    "breed": 4,
                    "owner": 6,
                    "birth_date": "2021-07-14",
                    "is_neutered": True,
                    "color": "laranja"
                }
            }
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

        self.stdout.write(self.style.SUCCESS('The database was successfully populated!'))
