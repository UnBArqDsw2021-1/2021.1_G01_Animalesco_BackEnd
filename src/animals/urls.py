from django.urls import include, path
from rest_framework_nested import routers

from .views import (BreedViewSet, PetViewSet, SpecieViewSet,
                    get_all_specie_breeds)

app_name = 'pets'

router = routers.DefaultRouter()

router.register(r'pets', PetViewSet)
router.register(r'species', SpecieViewSet)

# Aqui é onde criamos rotas nested. Na linha abaixo estamos criando um roteador dentro
# do contexto de species
specie_router = routers.NestedDefaultRouter(
    router,
    r"species",
    lookup="specie",
)

# Aqui definimos o contexto dos pets para rotas relacionadas com pets específicos
pets_router = routers.NestedDefaultRouter(
    router,
    r"pets",
    lookup="pet",
)

# Aqui estamos colocando as rotas de breeds dentro do contexto de species
specie_router.register(
    r"breeds",
    BreedViewSet,
    basename='breeds'
)

urlpatterns = [
    path("species-breeds/", get_all_specie_breeds),
    path("", include(router.urls)),
    path("", include(specie_router.urls)),
]
