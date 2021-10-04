from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .models import Pet, Specie, Breed

from .serializers import (
    PetSerializer,
    SpecieSerializer,
    BreedSerializer,
)


class SpecieViewSet(viewsets.ModelViewSet):
    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer
    doc_tags = ["Species"]

    # Nossa API permite que os usuários registre suas próprias espécies caso elas não
    # estejam cadastradas, porém essas novas espécies não são mostradas para os demais
    # usuários por padrão, enquanto o admin não verifique a veracidade dessas espécies.
    def get_queryset(self):
        queryset = Specie.objects.exclude(proven_veracity=False)
        return queryset

    def create(self, request, *args, **kwargs):
        from animals.tasks import test_func
        test_func.delay()
        return super().create(request, *args, **kwargs)

class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    doc_tags = ["Breeds"]

    # Como breed é uma controller nested (depende de uma specie), temos que sobrescrever
    # o get_queryset, pois assim determinado o contexto de acordo com a pk passada no
    # kwargs (url)
    def get_queryset(self):
        specie = get_object_or_404(Specie, pk=self.kwargs["specie_pk"])

        # Nossa API permite a criação de breeds pelos usuários, mas elas não são
        # mostradas para os demais usuários enquanto o admin não verifique a veracidade
        # dessas raças
        queryset = specie.breeds.all().exclude(proven_veracity=False)
        return queryset

    # Como breed é uma controller nested (depende de uma specie), temos que sobrescrever
    # o perform_create, pois assim sabemos o contexto da criação de acordo com a pk passada
    # no kwargs (url). Após pegar a pk, tentamos pegar a specie no banco de dados e passar
    # para a serializar responsável pela criação da Breed.
    def perform_create(self, serializer):
        specie = get_object_or_404(Specie, pk=self.kwargs["specie_pk"])
        serializer.save(specie=specie)

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    doc_tags = ["Pets"]

    def get_queryset(self):
        queryset = Pet.objects.filter(owner=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@swagger_auto_schema(
    tags=["Helpers"],
    method="get",
    operation_summary="Rota usada para consultar todas as Espécies e Raças cadastradas na backend",
)
@api_view(['GET',])
def get_all_specie_breeds(request):
    """
    Controller que irá retornar todas as espécies e raças que o frontend irá
    disponibilizar como opção de escolha

    Exemplo de json quer será retornado para o pessoal do front

    [
        {
            "specie_name": "Cachorro",
            "specie_pk": 1,
            "breeds": [
                {
                    "breed_name": "Pastor Alemão",
                    "breed_pk": 1
                },
                {
                    "breed_name": "Buldogue",
                    "breed_pk": 2
                }
            ]
        },

        {
            "specie_name": "Gato",
            "specie_pk": 2,
            "breeds": [
                {
                    "breed_name": "Persa",
                    "breed_pk": 3
                },
                {
                    "breed_name": "Siamês",
                    "breed_pk": 4
                }
            ]
        }
    ]
    """
    species = Specie.objects.all().prefetch_related('breeds')
    species = species.exclude(proven_veracity=False)

    data = list()

    for specie in species:
        breeds = specie.breeds.all()
        breeds = breeds.exclude(proven_veracity=False)

        specie_data = {
            "specie_name": specie.name,
            "specie_pk": specie.pk,
            "breeds": [
                {
                    "breed_name": breed.name,
                    "breed_pk": breed.pk,
                }
                for breed in breeds
            ]
        }

        data.append(specie_data)

    return Response(data, status=status.HTTP_200_OK)
