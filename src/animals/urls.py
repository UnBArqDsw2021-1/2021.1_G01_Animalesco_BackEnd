from rest_framework import routers
from animals.views import AnimalViewSet

router = routers.DefaultRouter()
router.register('animals', AnimalViewSet, basename='animals')

urlpatterns = router.urls
