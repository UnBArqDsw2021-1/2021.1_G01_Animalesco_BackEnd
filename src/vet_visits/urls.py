from django.urls import include, path

from vet_visits.views import VetVisitViewSet
from animals.urls import pets_router


app_name = 'vet_visits'

pets_router.register(
    r"vet_visits",
    VetVisitViewSet,
    basename='vet_visits',
)

urlpatterns = [
    path("", include(pets_router.urls)),
]
