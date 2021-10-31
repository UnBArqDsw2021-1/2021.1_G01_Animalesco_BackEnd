from django.urls import include, path

from animals.urls import pets_router
from vet_visits.views import VetVisitViewSet

app_name = 'vet_visits'

pets_router.register(
    r"vet_visits",
    VetVisitViewSet,
    basename='vet_visits',
)

urlpatterns = [
    path("", include(pets_router.urls)),
]
