from django.urls import include, path

from baths.views import BathViewSet
from animals.urls import pets_router

app_name = 'baths'

pets_router.register(
    r"baths",
    BathViewSet,
    basename='baths',
)

urlpatterns = [
    path("", include(pets_router.urls)),
]
