from django.urls import include, path

from rest_framework import routers
from animals.views import SpecieViewSet

router = routers.DefaultRouter()
router.register('species', SpecieViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
