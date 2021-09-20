from django.urls import include, path

from medicines.views import MedicineViewSet
from animals.urls import pets_router



app_name = 'medicines'

pets_router.register(
    r"medicines",
    MedicineViewSet,
    basename='medicines',
)

urlpatterns = [
    path("", include(pets_router.urls)),
]
