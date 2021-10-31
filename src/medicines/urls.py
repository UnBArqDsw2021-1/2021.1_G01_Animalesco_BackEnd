from django.urls import include, path

from animals.urls import pets_router
from medicines.views import MedicineViewSet

app_name = "medicines"

pets_router.register(
    r"medicines",
    MedicineViewSet,
    basename="medicines",
)

urlpatterns = [
    path("", include(pets_router.urls)),
]
