from djoser import views as djoser_views
from rest_framework_simplejwt import views as jwt_views


class UserViewSet(djoser_views.UserViewSet):
    doc_tags = ["Users"]

class TokenObtainPairView(jwt_views.TokenObtainPairView):
    doc_tags = ["JWT Auth"]

class TokenRefreshView(jwt_views.TokenRefreshView):
    doc_tags = ["JWT Auth"]

class TokenVerifyView(jwt_views.TokenVerifyView):
    doc_tags = ["JWT Auth"]

class TokenCreateView(djoser_views.TokenCreateView):
    doc_tags = ["Token Auth"]

class TokenDestroyView(djoser_views.TokenDestroyView):
    doc_tags = ["Token Auth"]
