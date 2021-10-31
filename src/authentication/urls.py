from django.urls import include, path, re_path
from rest_framework import routers

from authentication.views import (TokenCreateView, TokenDestroyView,
                                  TokenObtainPairView, TokenRefreshView,
                                  TokenVerifyView, UserViewSet)

router = routers.DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = [
    # Leia essa página para entender mais sobre o djoser
    # https://djoser.readthedocs.io/en/latest/getting_started.html

    path("", include(router.urls)),

    re_path(r"^jwt/create/?", TokenObtainPairView.as_view(), name="jwt-create"),
    re_path(r"^jwt/refresh/?", TokenRefreshView.as_view(), name="jwt-refresh"),
    re_path(r"^jwt/verify/?", TokenVerifyView.as_view(), name="jwt-verify"),

    re_path(r"^token/login/?$", TokenCreateView.as_view(), name="login"),
    re_path(r"^token/logout/?$", TokenDestroyView.as_view(), name="logout"),
]
