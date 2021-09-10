from django.db import router
from django.urls import include, path
from rest_framework_nested import routers

from vaccines.views import VaccineViewSet

app_name = 'vaccines'

router = routers.DefaultRouter()

router.register(r'vaccines', VaccineViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
