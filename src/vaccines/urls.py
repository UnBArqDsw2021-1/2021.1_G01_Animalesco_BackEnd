from django.urls import include, path

from animals.urls import pets_router
from vaccines.views import VaccineViewSet

app_name = 'vaccines'

pets_router.register(
    r"vaccines",
    VaccineViewSet,
    basename='vaccines',
)

urlpatterns = [
    path("", include(pets_router.urls)),
]
