from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

SchemaView = get_schema_view(
    openapi.Info(
        title="Animalesco API",
        default_version="v1",
        description="API REST para a app mobile Animalesco.",
        contact=openapi.Contact(email="animalesco.backend@animalesco.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


@api_view()
@permission_classes([permissions.AllowAny])
def healthcheck(request):
    """Endpoint para verificar a saúde do server"""
    return Response({"msg": "OK"})


urlpatterns = [
    path("", healthcheck),
    path("status/", healthcheck),
    path("admin/", admin.site.urls),
    re_path(
        r"^api/v1/docs/$",
        SchemaView.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^api/v1/docs/swagger/$",
        SchemaView.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^api/v1/docs/redoc/$",
        SchemaView.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path("api/v1/", include("authentication.urls")),
    path("api/v1/", include("animals.urls")),
    path("api/v1/", include("vaccines.urls")),
    path("api/v1/", include("medicines.urls")),
    path("api/v1/", include("vet_visits.urls")),
    path("api/v1/", include("baths.urls")),
]
