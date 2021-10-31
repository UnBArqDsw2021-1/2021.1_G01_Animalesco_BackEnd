from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from animals import admin_actions
from animals.models import Breed, Pet, Specie


@admin.register(Specie)
class SpecieAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "proven_veracity")
    search_fields = ("name",)
    list_filter = ("proven_veracity",)

    # Ações são funções que podem ser executadas sobre um conjunto de models. As ações
    # são acionadas via os dashboards do django admin
    actions = [
        admin_actions.mark_as_proven_veracity,
    ]


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "get_specie_name", "proven_veracity")
    search_fields = ("name",)
    list_filter = (
        "proven_veracity",
        "specie__name",
    )
    actions = [
        admin_actions.mark_as_proven_veracity,
    ]

    # Usamos a função get_queryset para sobrescrever o comportamento padrão do django
    # para obter dados do banco de dados. Aqui o compotamento sobrescrito é realizar um
    # inner join com a tabela specie durante a obtenção da lista de raças
    def get_queryset(self, request: HttpRequest) -> QuerySet:
        qs = super().get_queryset(request)
        qs = qs.prefetch_related("specie")
        return qs

    # A tabela Breed possui somente uma chave extrangeira de Specie, dessa forma temos
    # que fazer uma requisição para obter os demais atributos (nome por exemplo)
    def get_specie_name(self, obj: Breed) -> str:
        return obj.specie.name

    get_specie_name.short_description = "Specie"
    get_specie_name.admin_order_field = "specie__name"


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "get_breed_name",
        "get_specie_name",
        "sex",
        "birth_date",
        "is_neutered",
        "color",
    )
    search_fields = ("name",)
    list_filter = (
        "breed",
        "breed__specie__name",
        "sex",
    )

    # Usamos a função get_queryset para sobrescrever o comportamento padrão do django
    # para obter dados do banco de dados. Aqui o compotamento sobrescrito é realizar um
    # inner join com a tabela breed e specie durante a obtenção da lista de raças
    def get_queryset(self, request: HttpRequest) -> QuerySet:
        qs = super().get_queryset(request)
        qs = qs.prefetch_related("breed")
        qs = qs.prefetch_related("breed__specie")
        return qs

    def get_specie_name(self, obj: Pet) -> str:
        return obj.breed.specie.name

    get_specie_name.short_description = "Specie name"
    get_specie_name.admin_order_field = "breed__specie__name"

    def get_breed_name(self, obj: Pet) -> str:
        return obj.breed.name

    get_breed_name.short_description = "Breed name"
    get_breed_name.admin_order_field = "breed__name"
